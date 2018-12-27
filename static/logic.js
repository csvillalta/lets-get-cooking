$SCRIPT_ROOT = "http://127.0.0.1:5000";

$(document).ready(function(){
  $("#loading").hide()
  $("#title").hide()
  $("#instructions").hide()

  $(document).ajaxStart(function(){
    $("#title").hide();
    $("#instructions").hide();
    $("#get_recipe").hide()
    $("#loading").show();
  });

  $(document).ajaxStop(function(){
    $("#loading").hide();
    $("#title").show();
    $("#instructions").show();
    $("#get_recipe").show()
  });

  $("#get_recipe").click(function(){
    $.getJSON($SCRIPT_ROOT + "/_get_new_recipe", function(data){
      $("#title").html(data["title"]);
      $("#instructions").html(data["instructions"]);
    });
  });
});
