function Option_Gaokao(n)
{
  $("#id_high_sub"+n).empty();
  var option = new Array();
  option[0] = $("<option>").val("").text("Select Subject");
  option[1] = $("<option>").val("chinese").text("Chinese");
  option[2] = $("<option>").val("math").text("Math");
  option[3] = $("<option>").val("english").text("English");
  option[4] = $("<option>").val("combined_science").text("Combined Science");
  option[5] = $("<option>").val("combined_art").text("Combined Art");
  for(i=0;i<option.length;i++)
  {
    $("#id_high_sub"+n).append(option[i]);
  }
}

$(document).ready(function(){
                  var num_high_test = 1;
                  $("#id_high_test").change(function(){
                                            if ($("#id_high_test").val()=="Gaokao"){
                                            num_high_test=1;
                                            Option_Gaokao(num_high_test);
                                            }
                            });
                  $("#btn_high_test").click(function(){
                                            num_high_test++;
                                            $("#num_high_test").append('<div class="col-xs-4"> <div class="form-group"> <select class="form-control" id="id_high_sub'+num_high_test+'" name="high_sub'+num_high_test+'"> <option value="" selected="selected">Select Subject</option> </select> </div></div>');
                                            $("#num_high_test").append('<div class="col-xs-8"> <div class="form-group"> <input class="form-control" id="id_high_sub'+num_high_test+'_score" name="high_sub'+num_high_test+'_score" maxlength="50" name="one" type="text" placeholder="Score"/> </div> </div>');
                                            Option_Gaokao(num_high_test);
                                            });
                  });

