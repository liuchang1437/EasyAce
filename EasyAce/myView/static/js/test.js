function Option_Zhongkao(n)
{
	$("#id_middle_sub"+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select Subject");
	option[1] = $("<option>").val("chinese").text("Chinese");
	option[2] = $("<option>").val("math").text("Math");
	option[3] = $("<option>").val("english").text("English");
	option[4] = $("<option>").val("combined_science").text("Combined Science");
	option[5] = $("<option>").val("combined_art").text("Combined Art");
	for(i=0;i<option.length;i++)
	{
		$("#id_middle_sub"+n).append(option[i]);
	}
}

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
									var num_middle_test = 0;
									$("#id_middle_test").change(function(){
																						for(i=0;i<num_middle_test;i++)
																						{
																						$("#num_middle_test").find(".col-xs-4").eq(-1).remove();
																						$("#num_middle_test").find(".col-xs-8").eq(-1).remove();
																						}
																						num_middle_test=0;
																						});
									$("#btn_middle_test_add").click(function(){
																								if ($("#id_middle_test").val()!=""){
																								num_middle_test++;
																								$("#num_middle_test").append('<div class="col-xs-4"> <div class="form-group"> <select class="form-control" id="id_middle_sub'+num_middle_test+'" name="middle_sub'+num_middle_test+'"> <option value="" selected="selected">Select Subject</option> </select> </div></div>');
																								$("#num_middle_test").append('<div class="col-xs-8"> <div class="form-group"> <input class="form-control" id="id_middle_sub'+num_middle_test+'_score" name="middle_sub'+num_middle_test+'_score" maxlength="50" name="one" type="text" placeholder="Score"/> </div> </div>');
																								if ($("#id_middle_test").val()=="Zhongkao"){
																								Option_Zhongkao(num_middle_test);
																								}
																								}
																								});
									
									$("#btn_middle_test_remove").click(function(){
																									 if(num_middle_test>0) num_middle_test--;
																									 $("#num_middle_test").find(".col-xs-4").eq(-1).remove();
																									 $("#num_middle_test").find(".col-xs-8").eq(-1).remove();
																									 });
									
									
                  var num_high_test = 0;
                  $("#id_high_test").change(function(){
																						for(i=0;i<num_high_test;i++)
																						{
																							$("#num_high_test").find(".col-xs-4").eq(-1).remove();
																							$("#num_high_test").find(".col-xs-8").eq(-1).remove();
																						}
																						num_high_test=0;
                            });
                  $("#btn_high_test_add").click(function(){
																								if ($("#id_high_test").val()!=""){
																								num_high_test++;
																								$("#num_high_test").append('<div class="col-xs-4"> <div class="form-group"> <select class="form-control" id="id_high_sub'+num_high_test+'" name="high_sub'+num_high_test+'"> <option value="" selected="selected">Select Subject</option> </select> </div></div>');
																								$("#num_high_test").append('<div class="col-xs-8"> <div class="form-group"> <input class="form-control" id="id_high_sub'+num_high_test+'_score" name="high_sub'+num_high_test+'_score" maxlength="50" name="one" type="text" placeholder="Score"/> </div> </div>');
																								if ($("#id_high_test").val()=="Gaokao"){
																								Option_Gaokao(num_high_test);
																								}
																								}
                                            });
									
									$("#btn_high_test_remove").click(function(){
																								if(num_high_test>0) num_high_test--;
																								$("#num_high_test").find(".col-xs-4").eq(-1).remove();
																								$("#num_high_test").find(".col-xs-8").eq(-1).remove();
																									 });
                  });

