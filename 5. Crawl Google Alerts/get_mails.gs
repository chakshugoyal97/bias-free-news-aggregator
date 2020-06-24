/*
  Alerts were set up for the following key words:
 "aadhaar card"
 "aadhaarcard"
 "agrarian crisis"
 "agrarian unrest"
 "agricultural protest"
 "cash crunch"
 "cash withdrawal"
 "cashless economy"
 "crop loan"
 "currency switch"
 "debt waiver"
 "demonetised note"
 "farm loan"
 "farmer agitation"
 "Farmer distress"
 "farmer issue"
 "farmer issues"
 "farmer suicide"
 "farmers distress"
 "farmers issues"
 "farmers march"
 "Farmers plight"
 "Farmers protest"
 "Farmers' Protest"
 "Gabbar singh tax"
 "Goods and services tax"
 "goods service tax"
 "Kisaan long march"
 "Kisan long march"
 "note ban"
 "Notebandi"
 "plight farmer"
 "swipe machine"
 "adhaar"
 "adhar"
 "Demonetisation"
 "demonitisation"
 "GST"
 "uidai"
*/

function saveGmailAsPDF() {

  var gmailLabels  = "Alerts";
  var driveFolder  = "alerts_25"; 
  /* Keep iterating this. Had to do it manually because of execution time limit*/

  var threads = GmailApp.search("in:" + gmailLabels, 0, 500);

  if (threads.length > 0) {

    /* Google Drive folder where the Files would be saved */
    var folders = DriveApp.getFoldersByName(driveFolder);
    var folder = folders.hasNext() ?
        folders.next() : DriveApp.createFolder(driveFolder);

    /* Gmail Label that contains the queue */
    var label = GmailApp.getUserLabelByName(gmailLabels) ?
        GmailApp.getUserLabelByName(gmailLabels) : GmailApp.createLabel(driveFolder);

    for (var t=0; t<threads.length; t++) {

      threads[t].removeLabel(label);
      var msgs = threads[t].getMessages();

      var html = "";
      //var attachments = [];

      var subject = threads[t].getFirstMessageSubject();

      /* Append all the threads in a message in an HTML document */
      for (var m=0; m<msgs.length; m++) {

        var msg = msgs[m];

        html += "From: " + msg.getFrom() + "<br />";
        html += "To: " + msg.getTo() + "<br />";
        html += "Date: " + msg.getDate() + "<br />";
        html += "Subject: " + msg.getSubject() + "<br />";
        html += "<hr />";
        html += msg.getBody().replace(/<img[^>]*>/g,"");
        html += "<hr />";

        /*
        var atts = msg.getAttachments();
        for (var a=0; a<atts.length; a++) {
          attachments.push(atts[a]);
        }
        */
      }
      
      /* Save the attachment files and create links in the document's footer */
      /*
      if (attachments.length > 0) {
        var footer = "<strong>Attachments:</strong><ul>";
        for (var z=0; z<attachments.length; z++) {
          var file = folder.createFile(attachments[z]);
          footer += "<li><a href='" + file.getUrl() + "'>" + file.getName() + "</a></li>";
        }
        html += footer + "</ul>";
      }
      */
      
      /* Conver the Email Thread into a PDF File */
      var tempFile = DriveApp.createFile("temp.html", html, "text/html");
      folder.createFile(tempFile.getAs("application/pdf")).setName(subject + t + ".pdf");
      tempFile.setTrashed(true);

    }
  }
}