/// at time of making this, Qgenda only allows sync to external calendar
/// i wanted to add shifts to my personal calendar

function QGtoGCAL() {

    //source = cal ID of qgenda
    var source = CalendarApp.getCalendarById('XYZ@import.calendar.google.com');
    //googleCal ID
    var target = CalendarApp.getCalendarById('ABC@gmail.com');

    var today = new Date()
    var month = 9                                   // set month as nth month  -1
    var today_year = today.getFullYear();            // get this year
    var month = startPeriod.getMonth() + 1;
    startPeriod = new Date(today_year, month, 1);    //  set to start at first of month
    var endPeriod = new Date(today_year, month, 0);   // end of month

    var events = source.getEvents(startPeriod, endPeriod);

    // set counters
    var ccount = 0; //call
    var mcount = 0; //moonlight
    var bcount = 0; //benefit time
    var mshifts = "" // moonlight shift text
    var cshifts = "" // call shifts text 
    var bshifts = "" //bt time
    var body = "" // start of email body

    var calls = ["OC", "L1", "L3", "L4", "L1b", "oc", "BU", "OCB"]  //call shifts

    for (var i = 0; i < events.length; i++) {
        var event = events[i];
        var title = event.getTitle();
        for (call in calls) {
            var shift = calls[call];
            if (title.indexOf(shift) >= 0) {
                target.createAllDayEvent(title, event.getAllDayStartDate()).setColor("11"); //create event, set color to red
                Logger.log(title + " on " + event.getAllDayStartDate()); //log
                ccount++;
                cshifts += "- " + title + "on" + event.getAllDayStartDate() + "\n\n"; // add to email 
            }
        }
        if (title.indexOf("ERC") > -1) {
            target.createAllDayEvent(title, event.getAllDayStartDate()).setColor("2"); //create event, color mauve      
            Logger.log("ERC: " + title + "\s on \s " + event.getAllDayStartDate()); //log
            mcount++
            mshifts += "- " + title + "\s on \s" + event.getAllDayStartDate() + "\n\n"; // add to email 
        }
        if (title.indexOf("BT") > -1) {
            target.createAllDayEvent(title, event.getAllDayStartDate()).setColor("10"); //create event, color green
            Logger.log("BT: " + title + "\s on \s " + event.getAllDayStartDate()); //log
            bcount++
            bshifts += "- " + title + "\s on \s" + event.getAllDayStartDate() + "\n\n"; // add to email 
        }
    }
    Utilities.sleep(100);

    var recipient = Session.getActiveUser().getEmail();

    //tell me month
    var monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    month = monthNames[month]
    var subject = ccount + '//' + mcount + '//' + bcount + 'call/ERC/BT in ' + month;

    body += cshifts
    body += "\n"
    body += "----------------"
    body += "\n"
    body += mshifts
    body += "----------------"
    body += "\n"
    body += bshifts

    Logger.log(ccount + ' calls in ' + month)
    Logger.log(mcount + ' shifts in ' + month)
    Logger.log(bcount + ' time off in ' + month)
    MailApp.sendEmail(recipient, subject, body);
}


//references
//https://webapps.stackexchange.com/questions/108132/how-to-automatically-forward-events-from-one-google-calendar-to-another//
//https://script.google.com/d/1Z00KFsXZSLMYw1Tsf7gXqxEt4LjTYtyrnc0EHel43sHs6dl8_z5mHze2/edit //
//colors https://developers.google.com/apps-script/reference/calendar/event-color