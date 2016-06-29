function Option_AEIS(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("secondary english").text("Secondary English");
	option[2] = $("<option>").val("secondary maths").text("Secondary Maths");
	option[3] = $("<option>").val("primary english").text("Primary English");
	option[4] = $("<option>").val("primary maths").text("Primary Maths");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

function Option_OLEVEL(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("english language").text("English Language");
	option[2] = $("<option>").val("literature in english").text("Literature in English");
	option[3] = $("<option>").val("history").text("History");
	option[4] = $("<option>").val("combined humanities").text("Combined Humanities");
	option[5] = $("<option>").val("geography").text("Geography");
	option[6] = $("<option>").val("mathematics").text("Mathematics");
	option[7] = $("<option>").val("additional mathematics").text("Additional Mathematics");
	option[8] = $("<option>").val("physics-spa").text("Physics (SPA)");
	option[9] = $("<option>").val("chemistry-spa").text("Chemistry (SPA)");
	option[10] = $("<option>").val("science-physics-chemistry)").text("Science (Physics, Chemistry)");
	option[11] = $("<option>").val("science-physics-biology)").text("Science (Physics, Biology)");
	option[12] = $("<option>").val("science-chemistry-biology)").text("Science (Chemistry, Biology)");
	option[13] = $("<option>").val("biology-spa").text("Biology (SPA)");
	option[14] = $("<option>").val("art").text("Art");
	option[15] = $("<option>").val("principles of accounts").text("Principles of Accounts");
	option[16] = $("<option>").val("higher chinese").text("Higher Chinese");
	option[17] = $("<option>").val("chinese").text("Chinese");
	option[18] = $("<option>").val("literature in chinese").text("Literature in Chinese");
	option[19] = $("<option>").val("other").text("Other");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

function Option_ALEVEL(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("h1-general paper").text("H1-General Paper");
	option[2] = $("<option>").val("h1-project work").text("H1-Project Work");
	option[3] = $("<option>").val("h1-literature in english").text("H1-Literature in English");
	option[4] = $("<option>").val("h1-geography").text("H1-Geography");
	option[5] = $("<option>").val("h1-history").text("H1-History");
	option[6] = $("<option>").val("h1-china studies in english").text("H1-China Studies in English");
	option[7] = $("<option>").val("h1-economics").text("H1-Economics");
	option[8] = $("<option>").val("h1-mathematics").text("H1-Mathematics");
	option[9] = $("<option>").val("h1-physics").text("H1-Physics");
	option[10] = $("<option>").val("h1-chemistry").text("H1-Chemistry");
	option[11] = $("<option>").val("h1-biology").text("H1-Biology");
	option[12] = $("<option>").val("h1-chinese language").text("H1-Chinese Language");
	option[13] = $("<option>").val("h1-china studies in chinese").text("H1-China Studies in Chinese");
	option[14] = $("<option>").val("h1-general studies in chinese").text("H1-General Studies in Chinese");
	option[15] = $("<option>").val("h2-computing").text("H2-Computing");
	option[16] = $("<option>").val("h2-physics").text("H2-Physics");
	option[17] = $("<option>").val("h2-chemistry").text("H2-Chemistry ");
	option[18] = $("<option>").val("h2-biology").text("H2-Biology");
	option[19] = $("<option>").val("h2-geography").text("H2-Geography");
	option[20] = $("<option>").val("h2-history").text("H2-History");
	option[21] = $("<option>").val("h2-economics").text("H2-Economics");
	option[22] = $("<option>").val("h2-china studies in english").text("H2-China Studies in English");
	option[23] = $("<option>").val("h2-mathematics").text("H2-Mathematics");
	option[24] = $("<option>").val("h2-literature in english").text("H2-literature in english");
	option[25] = $("<option>").val("h2-principles of accounting").text("H2-Principles of Accounting");
	option[26] = $("<option>").val("h2-knowledge and inquiry").text("H2-Knowledge and Inquiry");
	option[27] = $("<option>").val("h2-chinese language and literature").text("H2-Chinese Language and Literature");
	option[28] = $("<option>").val("h2-china studies in chinese").text("H2-China Studies in Chinese");
	option[29] = $("<option>").val("h3-economics").text("H3-Economics");
	option[30] = $("<option>").val("h3-mathematics").text("H3-Mathematics");
	option[31] = $("<option>").val("other").text("Other");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

function Option_IB_MYP(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("language acquisition").text("Language acquisition");
	option[2] = $("<option>").val("economics").text("Economics");
	option[3] = $("<option>").val("physical sciences").text("Physical sciences");
	option[4] = $("<option>").val("standard mathematics").text("Standard mathematics");
	option[5] = $("<option>").val("extended mathematics").text("Extended mathematics");
	option[6] = $("<option>").val("other").text("Other");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

function Option_IB_DP(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("theory of knowledge").text("Theory of knowledge");
	option[2] = $("<option>").val("language a: literature").text("Language A: literature (SL/HL)");
	option[3] = $("<option>").val("language a: language and literature").text("Language A: language and literature (SL/HL)");
	option[4] = $("<option>").val("business management").text("Business management (SL/HL)");
	option[5] = $("<option>").val("economics").text("Economics (SL/HL)");
	option[6] = $("<option>").val("biology").text("Biology (SL/HL)");
	option[7] = $("<option>").val("chemistry").text("Chemistry (SL/HL)");
	option[8] = $("<option>").val("physics").text("Physics (SL/HL)");
	option[9] = $("<option>").val("mathematics").text("Mathematics (SL/HL)");
	option[10] = $("<option>").val("further mathematics").text("Further mathematics (HL)");
	option[11] = $("<option>").val("other").text("Other");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

function Option_Zhongkao(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("chinese").text("Chinese");
	option[2] = $("<option>").val("mathematics").text("Mathematics");
	option[3] = $("<option>").val("english").text("English");
	option[4] = $("<option>").val("physics").text("Physics");
	option[5] = $("<option>").val("chemistry").text("Chemistry");
	option[6] = $("<option>").val("biology").text("Biology");
	option[7] = $("<option>").val("history").text("History");
	option[8] = $("<option>").val("geography").text("Geography");
	option[9] = $("<option>").val("politics").text("Politics");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

function Option_Gaokao(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("chinese").text("Chinese");
	option[2] = $("<option>").val("math").text("Math");
	option[3] = $("<option>").val("english").text("English");
	option[4] = $("<option>").val("combined science").text("Combined Science");
	option[5] = $("<option>").val("combined humanity").text("Combined Humanity");
	option[6] = $("<option>").val("physics").text("Physics");
	option[7] = $("<option>").val("chemistry").text("Chemistry");
	option[8] = $("<option>").val("biology").text("Biology");
	option[9] = $("<option>").val("history").text("History");
	option[10] = $("<option>").val("geography").text("Geography");
	option[911] = $("<option>").val("politics").text("Politics");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

function Option_SAT(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("chinese").text("Chinese");
	option[2] = $("<option>").val("math").text("Math");
	option[3] = $("<option>").val("english").text("English");
	option[4] = $("<option>").val("???").text("???");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
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
																									if ($("#id_middle_test").val()=="aeis"){
																									Option_AEIS("#id_middle_sub",num_middle_test);
																									}
																									if ($("#id_middle_test").val()=="o-level"){
																									Option_OLEVEL("#id_middle_sub",num_middle_test);
																									}
																									if ($("#id_middle_test").val()=="ib-myp"){
																									Option_IB_MYP("#id_middle_sub",num_middle_test);
																									}
																									if ($("#id_middle_test").val()=="zhongkao"){
																									Option_Zhongkao("#id_middle_sub",num_middle_test);
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
																								if ($("#id_high_test").val()=="a-level"){
																								Option_ALEVEL("#id_high_sub",num_high_test);
																								}
																								if ($("#id_high_test").val()=="ib-dp"){
																								Option_IB_DP("#id_high_sub",num_high_test);
																								}
																								if ($("#id_high_test").val()=="gaokao"){
																								Option_Gaokao("#id_high_sub",num_high_test);
																								}
																								if ($("#id_high_test").val()=="sat"){
																								Option_SAT("#id_high_sub",num_high_test);
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


