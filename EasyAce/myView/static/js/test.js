function Option_Zhongkao(n)
{
	$("#id_middle_sub"+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
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
  option[0] = $("<option>").val("").text("Select subject");
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

function Option_Teaching_Level(n)
{
	$("#id_teaching_level"+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select teaching level");
	option[1] = $("<option>").val("a-level").text("A-LEVEL");
	option[2] = $("<option>").val("o-level").text("O-LEVEL");
	option[3] = $("<option>").val("gaokao").text("Gaokao");
	option[4] = $("<option>").val("zhongkao").text("Zhongkao");
	for(i=0;i<option.length;i++)
	{
		$("#id_teaching_level"+n).append(option[i]);
	}
}

function Option_Teaching_Gaokao(n)
{
	$("#id_teaching_sub"+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select teaching subject");
	option[1] = $("<option>").val("chinese").text("Chinese");
	option[2] = $("<option>").val("math").text("Math");
	option[3] = $("<option>").val("english").text("English");
	option[4] = $("<option>").val("combined_science").text("Combined Science");
	option[5] = $("<option>").val("combined_art").text("Combined Art");
	for(i=0;i<option.length;i++)
	{
		$("#id_teaching_sub"+n).append(option[i]);
	}
}

$(document).ready(function(){
									$("#btn_middle_test").hide();
									var num_middle_test = 0;
									$("#id_middle_test").change(function(){
																							for(i=0;i<num_middle_test;i++)
																							{
																							$("#num_middle_test").find(".col-xs-4").eq(-1).remove();
																							$("#num_middle_test").find(".col-xs-8").eq(-1).remove();
																							}
																							num_middle_test=0;
																							$("#btn_middle_test").hide();
																							if ($("#id_middle_test").val()!=""){
																							$("#btn_middle_test_add").click();
																							$("#btn_middle_test").show();
																							}
																							});
									$("#btn_middle_test_add").click(function(){
																								if ($("#id_middle_test").val()!=""){
																								num_middle_test++;
																								$("#num_middle_test").append('<div class="col-xs-4"> <div class="form-group"> <select class="form-control" id="id_middle_sub'+num_middle_test+'" name="middle_sub'+num_middle_test+'"> <option value="" selected="selected">Select subject</option> </select> </div></div>');
																								$("#num_middle_test").append('<div class="col-xs-8"> <div class="form-group"> <input class="form-control" id="id_middle_sub'+num_middle_test+'_score" name="middle_sub'+num_middle_test+'_score" maxlength="50" name="one" type="text" placeholder="Score"/> </div> </div>');
																								if ($("#id_middle_test").val()=="zhongkao"){
																								Option_Zhongkao(num_middle_test);
																								}
																								}
																								});
									
									$("#btn_middle_test_remove").click(function(){
																										 if(num_middle_test>1){
																										 num_middle_test--;
																										 $("#num_middle_test").find(".col-xs-4").eq(-1).remove();
																										 $("#num_middle_test").find(".col-xs-8").eq(-1).remove();
																										 }
																										 });
									
									
									$("#btn_high_test").hide();
                  var num_high_test = 0;
                  $("#id_high_test").change(function(){
																						for(i=0;i<num_high_test;i++)
																						{
																							$("#num_high_test").find(".col-xs-4").eq(-1).remove();
																							$("#num_high_test").find(".col-xs-8").eq(-1).remove();
																						}
																						num_high_test=0;
																						$("#btn_high_test").hide();
																						if ($("#id_high_test").val()!=""){
																						$("#btn_high_test_add").click();
																						$("#btn_high_test").show();
																						}
																						});
                  $("#btn_high_test_add").click(function(){
																								if ($("#id_high_test").val()!=""){
																								num_high_test++;
																								$("#num_high_test").append('<div class="col-xs-4"> <div class="form-group"> <select class="form-control" id="id_high_sub'+num_high_test+'" name="high_sub'+num_high_test+'"> <option value="" selected="selected">Select subject</option> </select> </div></div>');
																								$("#num_high_test").append('<div class="col-xs-8"> <div class="form-group"> <input class="form-control" id="id_high_sub'+num_high_test+'_score" name="high_sub'+num_high_test+'_score" maxlength="50" name="one" type="text" placeholder="Score"/> </div> </div>');
																								if ($("#id_high_test").val()=="gaokao"){
																								Option_Gaokao(num_high_test);
																								}
																								}
                                            });
									
									$("#btn_high_test_remove").click(function(){
																									 if(num_high_test>1){
																									 num_high_test--;
																									 $("#num_high_test").find(".col-xs-4").eq(-1).remove();
																									 $("#num_high_test").find(".col-xs-8").eq(-1).remove();
																									 }
																									 });
									
									var num_teaching_level = 1;
									$("#btn_teaching_level_add").click(function(){
																										 if(num_teaching_level<10){
																										 num_teaching_level++;
																										 $("#num_teaching_level").append('<div class="row"> <div class="col-xs-4"> <div class="form-group"> <select class="form-control" id="id_teaching_level'+num_teaching_level+'" name="teaching_level'+num_teaching_level+'"> <option value="" selected="selected">Select teaching level</option> </select> </div> </div> <div class="col-xs-4"> <div class="form-group"> <div id="num_teaching_sub'+num_teaching_level+'"></div> </div> </div> </div>');
																										 Option_Teaching_Level(num_teaching_level);
																										 }
																								});
									
									$("#btn_teaching_level_remove").click(function(){
																											 if(num_teaching_level>1){
																											 num_teaching_level--;
																											 $("#num_teaching_level").find(".row").eq(-1).remove();
																											 }
																											 });

									
									for(i=1;i<=10;i++){
									(function(i){
									 $(document).change("#id_teaching_level"+i,function(){
																		 $("#num_teaching_sub"+i).empty();
																		 if ($("#id_teaching_level"+i).val()=="gaokao"){
																		 $("#num_teaching_sub"+i).append('<select class="form-control" id="id_teaching_sub'+i+'" name="teaching_sub'+i+'"> </select>');
																		 Option_Teaching_Gaokao(i);
																		 }
																		 });
									 })(i)
									}


									
									
                  });


