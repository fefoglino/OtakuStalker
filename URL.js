// var gay=$("input").val;
// var request="http://localhost:5000/screenname/api/v1.0/analysis/"+gay;
// // var img_add="http://localhost:5000/screenname/api/v1.0/analysis/"+gay+ "wordcloud";
function wlw(){
  fetch(request)
    .then(function(response) {
      return response.json();
    })
    .then(function(myJson) {
      // var mch=myJson[0]["mostCommonHashtags"];
      var pf=myJson[0]["problematicFactor"];
      var retweet=myJson[0]["totalRetweets"];
      var frequency=myJson[0]["tweetFrequency"];
      if (myJson[0]["mostUsedWords"]===0){
        var words = "Not enough words to analyze";
        document.getElementById('wordscaption').innerHTML="Most Commonly Used Words: "+words;
      } else {
        document.getElementById('wordscaption').innerHTML="Most Commonly Used Words: ";
        var htmlCode = " ";
        for (i=0; i<50; i++) {
          htmlCode += "<li>"+myJson[0]["mostUsedWords"][i]+"</li>";
        }
        document.getElementById("words").innerHTML=htmlCode
      }
      if (myJson[0]["mostCommonHashtags"]===0){
        var insertext = "Not enough hashtags to analyze";
        document.getElementById('hashtagscaption').innerHTML="Most Commonly Used Hashtags: "+insertext;
      } else {
        document.getElementById('hashtagscaption').innerHTML="Most Commonly Used Hashtags: ";
        var hashtagsCode = " ";
        for (i=0; i<5; i++) {
          hashtagsCode += "<li>"+myJson[0]["mostCommonHashtags"][i]+"</li>";
        }
        document.getElementById("hashtags").innerHTML=hashtagsCode
      }
      // document.getElementById('hashtags').innerHTML="Most Used Hashtags: "+mch;
      document.getElementById('problematic').innerHTML="Problematic Factor from 1-10: "+pf;
      document.getElementById('rate').innerHTML="Average Number of Hours Between Tweets: "+frequency;
      document.getElementById('retweets').innerHTML="Total Number of Retweets: "+retweet;


      // document.getElementById("in").style.margin.bottom="0px";
      console.log(myJson);

    });
  }
  // function fetchim(img_address){
  //     fetch(img_address).then(function(response){
  //         if (response.ok){
  //             response.blob().then(function(blob){
  //                 var image_URL = URL.createObjectURL(blob);
  //                 // var image = document.getElementById("textblob");
  //                 // image.src = image_URL;
  //                 document.getElementById('textblob').src=image_URL;
  //             });
  //         } else {
  //             alert(response.statusText);
  //         }
  //     });
  // }



  function daddio(){
    gay = document.getElementById("twitter_handle").value;
    request="http://localhost:5000/screenname/api/v1.0/analysis/"+gay;
    // img_add="http://localhost:5000/screenname/api/v1.0/analysis/"+gay+ "wordcloud";
    wlw();
    // fetchim(img_add);
  }
