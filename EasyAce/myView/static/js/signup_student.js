function Option_Gaokao(n)
{
  $("#id_student_subject"+n).empty();
  var option = new Array();
  option[0] = $("<option>").val("").text("Select subject");
  option[1] = $("<option>").val("chinese").text("Chinese");
  option[2] = $("<option>").val("math").text("Math");
  option[3] = $("<option>").val("english").text("English");
  option[4] = $("<option>").val("combined_science").text("Combined Science");
  option[5] = $("<option>").val("combined_art").text("Combined Art");
  for(i=0;i<option.length;i++)
  {
    $("#id_student_subject"+n).append(option[i]);
  }
}

$(document).ready(function(){
									$("#btn_student_subject").hide();
                  var num_student_subject = 0;
                  $("#id_student_subject").change(function(){
																						for(i=0;i<num_student_subject;i++)
																						{
																							$("#num_student_subject").find(".col-xs-12").eq(-1).remove();
																						}
																						num_student_subject=0;
																						$("#btn_student_subject").hide();
																						if ($("#id_student_subject").val()!=""){
																						$("#btn_student_subject_add").click();
																						$("#btn_student_subject").show();
																						}
																						});
                  $("#btn_student_subject_add").click(function(){
																								if ($("#id_student_subject").val()!="" && num_student_subject<5){
																								num_student_subject++;
																								$("#num_student_subject").append('<div class="col-xs-12"> <div class="form-group"> <select class="form-control" id="id_student_subject'+num_student_subject+'" name="student_subject'+num_student_subject+'"> <option value="" selected="selected">Select subject</option> </select> </div></div>');
																								if ($("#id_student_subject").val()=="gaokao"){
																								Option_Gaokao(num_student_subject);
																								}
																								}
                                            });
									
									$("#btn_student_subject_remove").click(function(){
																									 if(num_student_subject>1){
																									 num_student_subject--;
																									 $("#num_student_subject").find(".col-xs-12").eq(-1).remove();
																									 }
																									 });
									
									$("#id_student_start_time").change(function(){
																										 if($("#id_student_start_time").val()=="other"){
																										 $("#id_student_start_time_other").append('<input class="form-control" id="id_student_start_time_other" type="date" name="student_start_time_other"/>');
																										 }
																										 else{
																										 $("#id_student_start_time_other").empty();
																										 }
																									});
									
									var num_click = 0;
									$("#id_student_remark5").click(function(){
																								 if(num_click==0){
																								 $("#id_remark_other").append('<textarea class="form-control" id="id_student_remark_other" name="student_remark_other" rows="3" placeholder="Other Remarks"></textarea>');
																								 num_click=1;
																								 }
																								 else{
																								 $("#id_remark_other").empty();
																								 num_click=0;
																								 }
																								});
									
									});


