function Option_PSLE(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("english").text("English");
	option[2] = $("<option>").val("chinese").text("Chinese");
	option[3] = $("<option>").val("higher chinese").text("Higher Chinese");
	option[4] = $("<option>").val("science").text("Science");
	option[5] = $("<option>").val("mathematics").text("Mathematics");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

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

function Option_OLEVEL_OTHER(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("arabic as a 3rd language").text("Arabic as a 3rd Language");
	option[2] = $("<option>").val("bahasa indonesia as a 3rd language").text("Bahasa Indonesia as a 3rd Language");
	option[3] = $("<option>").val("french").text("French");
	option[4] = $("<option>").val("german").text("German");
	option[5] = $("<option>").val("hindi").text("Hindi");
	option[6] = $("<option>").val("urdu").text("Urdu");
	option[7] = $("<option>").val("gujarati").text("Gujarati");
	option[8] = $("<option>").val("panjabi").text("Panjabi");
	option[9] = $("<option>").val("bengali").text("Bengali");
	option[10] = $("<option>").val("burmese").text("Burmese");
	option[11] = $("<option>").val("thai").text("Thai");
	option[12] = $("<option>").val("japanese").text("Japanese");
	option[13] = $("<option>").val("mathematics revised").text("Mathematics Revised");
	option[14] = $("<option>").val("music").text("Music");
	option[15] = $("<option>").val("higher music").text("Higher Music");
	option[16] = $("<option>").val("food and nutrition").text("Food and Nutrition");
	option[17] = $("<option>").val("higher art").text("Higher Art");
	option[18] = $("<option>").val("design and technology").text("Design and Technology");
	option[19] = $("<option>").val("economics").text("Economics");
	option[20] = $("<option>").val("drama").text("Drama");
	option[21] = $("<option>").val("physical education").text("Physical Education");
	option[22] = $("<option>").val("computer studies").text("Computer Studies");
	option[23] = $("<option>").val("business studies").text("Business Studies");
	option[24] = $("<option>").val("fundamentals of electronics").text("Fundamentals of Electronics");
	option[25] = $("<option>").val("media studies").text("Media Studies");
	option[26] = $("<option>").val("biotechnology").text("Biotechnology");
	option[27] = $("<option>").val("design studies").text("Design Studies");
	option[28] = $("<option>").val("media studies").text("Media Studies");
	option[29] = $("<option>").val("introduction to enterprise development").text("Introduction to Enterprise Development ");
	option[30] = $("<option>").val("malay").text("Malay");
	option[31] = $("<option>").val("tamil").text("Tamil");

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

function Option_ALEVEL_OTHER(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("h1-bengali").text("H1-Bengali");
	option[2] = $("<option>").val("h1-gujarati").text("H1-Gujarati");
	option[3] = $("<option>").val("h1-hindi").text("H1-Hindi");
	option[4] = $("<option>").val("h1-french").text("H1-French");
	option[5] = $("<option>").val("h1-german").text("H1-German");
	option[6] = $("<option>").val("h1-japanese").text("H1-Japanese");
	option[7] = $("<option>").val("h1-panjabi").text("H1-Panjabi");
	option[8] = $("<option>").val("h1-urdu").text("H1-Urdu");
	option[9] = $("<option>").val("h1-malay language").text("H1-Malay Language");
	option[10] = $("<option>").val("h1-tamil language").text("H1-Tamil Language");
	option[11] = $("<option>").val("h1-art").text("H1-Art");
	option[12] = $("<option>").val("h2-translation-chinese").text("H2-Translation (Chinese)");
	option[13] = $("<option>").val("h2-theatre studies and drama").text("H2-Theatre Studies and Drama");
	option[14] = $("<option>").val("h2-english language and linguistics").text("H2-English Language and Linguistics");
	option[15] = $("<option>").val("h2-french").text("H2-French");
	option[16] = $("<option>").val("h2-german").text("H2-German");
	option[17] = $("<option>").val("h2-japanese").text("H2-Japanese");
  option[18] = $("<option>").val("h2-art").text("H2-Art");
	option[19] = $("<option>").val("h2-music").text("H2-Music");
	option[20] = $("<option>").val("h2-management of business").text("H2-Management of Business");
	option[21] = $("<option>").val("h3-literature in english").text("H3-Literature in English");
	option[22] = $("<option>").val("h3-geography").text("H3-Geography");
	option[23] = $("<option>").val("h3-history").text("H3-History");
	option[24] = $("<option>").val("h3-essentials of modern physics").text("H3-Essentials of Modern Physics");
	option[25] = $("<option>").val("h3-pharmaceutical chemistry").text("H3-Pharmaceutical Chemistry");
	option[26] = $("<option>").val("h3-proteomics").text("H3-Proteomics");
	option[27] = $("<option>").val("h3-art").text("H3-Art");
	option[28] = $("<option>").val("h3-music").text("H3-Music");
	option[29] = $("<option>").val("h3-chinese language and literature").text("H3-Chinese Language and Literature");
	

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

function Option_IB_MYP_OTHER(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("language and literature").text("Language and literature");
	option[2] = $("<option>").val("individuals and societies").text("Individuals and societies");
	option[3] = $("<option>").val("world, local or national history").text("world, local or national history");
	option[4] = $("<option>").val("geography").text("geography");
	option[5] = $("<option>").val("global politics or international relations").text("global politics or international relations");
	option[6] = $("<option>").val("civics").text("civics");
	option[7] = $("<option>").val("philosophy").text("philosophy");
	option[8] = $("<option>").val("business management").text("business management");
	option[9] = $("<option>").val("sociology").text("sociology");
	option[10] = $("<option>").val("psychology").text("psychology");
	option[11] = $("<option>").val("anthropology").text("anthropology");
	option[12] = $("<option>").val("life sciences").text("life sciences");
	option[13] = $("<option>").val("health sciences").text("health sciences");
	option[14] = $("<option>").val("earth sciences").text("earth sciences");
	
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

function Option_IB_DP_OTHER(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("the extended essay ").text("The extended essay ");
	option[2] = $("<option>").val("creativity, activity, service").text("Creativity, activity, service");
	option[3] = $("<option>").val("literature and performance").text("Literature and performance (SL)");
	option[4] = $("<option>").val("geography").text("geography (SL/HL)");
	option[5] = $("<option>").val("global politics").text("global politics (SL/HL)");
	option[6] = $("<option>").val("history").text("history (SL/HL)");
	option[7] = $("<option>").val("philosophy").text("philosophy (SL/HL)");
	option[8] = $("<option>").val("psychology").text("psychology (SL/HL)");
	option[9] = $("<option>").val("computer science").text("computer science (SL/HL)");
	option[10] = $("<option>").val("mathematical studies standard level").text("mathematical studies standard level (SL/HL) ");

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

$(document).ready(function(){
									$("#btn_student_subject").hide();
                  var num_student_subject = 0;
                  $("#id_student_subject").change(function(){
																						for(i=0;i<num_student_subject;i++)
																						{
																							$("#num_student_subject").find(".col-xs-6").eq(-1).remove();
																							$("#num_student_subject").find(".col-xs-6").eq(-1).remove();
																						}
																						num_student_subject=0;
																						$("#btn_student_subject").hide();
																						if ($("#id_student_subject").val()!=""){
																						$("#btn_student_subject_add").click();
																						$("#btn_student_subject").show();
																						}
																						});
									for(i=1;i<=10;i++){
									(function(i){
									 $(document).change("#id_student_subject"+i,function(){
																		 $("#num_student_subject_other"+i).empty();
																		 if ($("#id_student_subject"+i).val()=="other"){
																		 $("#num_student_subject_other"+i).append('<div class="col-xs-6"> <div class="form-group"> <input class="form-control" id="id_student_subject_other" maxlength="50" name="student_subject_other" type="text" placeholder="Input subjects"/> </div> </div>');
																		 }
																		 });
									 })(i)
									}
									
                  $("#btn_student_subject_add").click(function(){
																											if ($("#id_student_subject").val()!="" && num_student_subject<10){
																											num_student_subject++;
																											$("#num_student_subject").append('<div class="row"> <div class="col-xs-6"> <div class="form-group"> <select class="form-control" id="id_student_subject'+num_student_subject+'" name="student_subject'+num_student_subject+'"> <option value="" selected="selected">Select subject</option> </select> </div></div> <div id="num_student_subject_other'+num_student_subject+'"></div> </div>');
																											if ($("#id_student_subject").val()=="psle"){
																											Option_PSLE("#id_student_subject",num_student_subject);
																											}
																											if ($("#id_student_subject").val()=="aeis"){
																											Option_AEIS("#id_student_subject",num_student_subject);
																											}
																											if ($("#id_student_subject").val()=="o-level"){
																											Option_OLEVEL("#id_student_subject",num_student_subject);
																											}
																											if ($("#id_student_subject").val()=="a-level"){
																											Option_ALEVEL("#id_student_subject",num_student_subject);
																											}
																											if ($("#id_student_subject").val()=="ib-myp"){
																											Option_IB_MYP("#id_student_subject",num_student_subject);
																											}
																											if ($("#id_student_subject").val()=="ib-dp"){
																											Option_IB_DP("#id_student_subject",num_student_subject);
																											}
																											if ($("#id_student_subject").val()=="zhongkao"){
																											Option_Zhongkao("#id_student_subject",num_student_subject);
																											}
																											if ($("#id_student_subject").val()=="gaokao"){
																											Option_Gaokao("#id_student_subject",num_student_subject);
																											}
																											if ($("#id_student_subject").val()=="sat"){
																											Option_SAT("#id_student_subject",num_student_subject);
																											}
																								}
                                            });
									
									$("#btn_student_subject_remove").click(function(){
																									 if(num_student_subject>1){
																									 num_student_subject--;
																									 $("#num_student_subject").find(".col-xs-6").eq(-1).remove();
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


