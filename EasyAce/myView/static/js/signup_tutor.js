function Option_PSLE(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("English").text("English");
	option[2] = $("<option>").val("Chinese").text("Chinese");
	option[3] = $("<option>").val("Higher Chinese").text("Higher Chinese");
	option[4] = $("<option>").val("Science").text("Science");
	option[5] = $("<option>").val("Mathematics").text("Mathematics");
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
	option[1] = $("<option>").val("Secondary English").text("Secondary English");
	option[2] = $("<option>").val("Secondary Maths").text("Secondary Maths");
	option[3] = $("<option>").val("Primary English").text("Primary English");
	option[4] = $("<option>").val("Primary Maths").text("Primary Maths");
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
	option[1] = $("<option>").val("English Language").text("English Language");
	option[2] = $("<option>").val("Literature in English").text("Literature in English");
	option[3] = $("<option>").val("History").text("History");
	option[4] = $("<option>").val("Combined Humanities").text("Combined Humanities");
	option[5] = $("<option>").val("Geography").text("Geography");
	option[6] = $("<option>").val("Mathematics").text("Mathematics");
	option[7] = $("<option>").val("Additional Mathematics").text("Additional Mathematics");
	option[8] = $("<option>").val("Physics (SPA)").text("Physics (SPA)");
	option[9] = $("<option>").val("Chemistry (SPA)").text("Chemistry (SPA)");
	option[10] = $("<option>").val("Science (Physics, Chemistry)").text("Science (Physics, Chemistry)");
	option[11] = $("<option>").val("Science (Physics, Biology)").text("Science (Physics, Biology)");
	option[12] = $("<option>").val("Science (Chemistry, Biology)").text("Science (Chemistry, Biology)");
	option[13] = $("<option>").val("Biology (SPA)").text("Biology (SPA)");
	option[14] = $("<option>").val("Art").text("Art");
	option[15] = $("<option>").val("Principles of Accounts").text("Principles of Accounts");
	option[16] = $("<option>").val("Higher Chinese").text("Higher Chinese");
	option[17] = $("<option>").val("Chinese").text("Chinese");
	option[18] = $("<option>").val("Literature in Chinese").text("Literature in Chinese");
	option[19] = $("<option>").val("Other").text("Other");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

function Option_OLEVEL_OTHER(s)
{
	$(s).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("Arabic as a 3rd Language").text("Arabic as a 3rd Language");
	option[2] = $("<option>").val("Bahasa Indonesia as a 3rd Language").text("Bahasa Indonesia as a 3rd Language");
	option[3] = $("<option>").val("French").text("French");
	option[4] = $("<option>").val("German").text("German");
	option[5] = $("<option>").val("Hindi").text("Hindi");
	option[6] = $("<option>").val("Urdu").text("Urdu");
	option[7] = $("<option>").val("Gujarati").text("Gujarati");
	option[8] = $("<option>").val("Panjabi").text("Panjabi");
	option[9] = $("<option>").val("Bengali").text("Bengali");
	option[10] = $("<option>").val("Burmese").text("Burmese");
	option[11] = $("<option>").val("Thai").text("Thai");
	option[12] = $("<option>").val("Japanese").text("Japanese");
	option[13] = $("<option>").val("Mathematics Revised").text("Mathematics Revised");
	option[14] = $("<option>").val("Music").text("Music");
	option[15] = $("<option>").val("Higher Music").text("Higher Music");
	option[16] = $("<option>").val("Food and Nutrition").text("Food and Nutrition");
	option[17] = $("<option>").val("Higher Art").text("Higher Art");
	option[18] = $("<option>").val("Design and Technology").text("Design and Technology");
	option[19] = $("<option>").val("Economics").text("Economics");
	option[20] = $("<option>").val("Drama").text("Drama");
	option[21] = $("<option>").val("Physical Education").text("Physical Education");
	option[22] = $("<option>").val("Computer Studies").text("Computer Studies");
	option[23] = $("<option>").val("Business Studies").text("Business Studies");
	option[24] = $("<option>").val("Fundamentals of Electronics").text("Fundamentals of Electronics");
	option[25] = $("<option>").val("Media Studies").text("Media Studies");
	option[26] = $("<option>").val("Biotechnology").text("Biotechnology");
	option[27] = $("<option>").val("Design Studies").text("Design Studies");
	option[28] = $("<option>").val("Media Studies").text("Media Studies");
	option[29] = $("<option>").val("Introduction to Enterprise Development").text("Introduction to Enterprise Development ");
	option[30] = $("<option>").val("Malay").text("Malay");
	option[31] = $("<option>").val("Tamil").text("Tamil");
	
	for(i=0;i<option.length;i++)
	{
		$(s).append(option[i]);
	}
}

function Option_ALEVEL(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("H1-General Paper").text("H1-General Paper");
	option[2] = $("<option>").val("H1-Project Work").text("H1-Project Work");
	option[3] = $("<option>").val("H1-Literature in English").text("H1-Literature in English");
	option[4] = $("<option>").val("H1-Geography").text("H1-Geography");
	option[5] = $("<option>").val("H1-History").text("H1-History");
	option[6] = $("<option>").val("H1-China Studies in English").text("H1-China Studies in English");
	option[7] = $("<option>").val("H1-Economics").text("H1-Economics");
	option[8] = $("<option>").val("H1-Mathematics").text("H1-Mathematics");
	option[9] = $("<option>").val("H1-Physics").text("H1-Physics");
	option[10] = $("<option>").val("H1-Chemistry").text("H1-Chemistry");
	option[11] = $("<option>").val("H1-Biology").text("H1-Biology");
	option[12] = $("<option>").val("H1-Chinese Language").text("H1-Chinese Language");
	option[13] = $("<option>").val("H1-China Studies in Chinese").text("H1-China Studies in Chinese");
	option[14] = $("<option>").val("H1-General Studies in Chinese").text("H1-General Studies in Chinese");
	option[15] = $("<option>").val("H2-Computing").text("H2-Computing");
	option[16] = $("<option>").val("H2-Physics").text("H2-Physics");
	option[17] = $("<option>").val("H2-Chemistry").text("H2-Chemistry ");
	option[18] = $("<option>").val("H2-Biology").text("H2-Biology");
	option[19] = $("<option>").val("H2-Geography").text("H2-Geography");
	option[20] = $("<option>").val("H2-History").text("H2-History");
	option[21] = $("<option>").val("H2-Economics").text("H2-Economics");
	option[22] = $("<option>").val("H2-China Studies in English").text("H2-China Studies in English");
	option[23] = $("<option>").val("H2-Mathematics").text("H2-Mathematics");
	option[24] = $("<option>").val("H2-Literature in English").text("H2-Literature in English");
	option[25] = $("<option>").val("H2-Principles of Accounting").text("H2-Principles of Accounting");
	option[26] = $("<option>").val("H2-Knowledge and Inquiry").text("H2-Knowledge and Inquiry");
	option[27] = $("<option>").val("H2-Chinese Language and Literature").text("H2-Chinese Language and Literature");
	option[28] = $("<option>").val("H2-China Studies in Chinese").text("H2-China Studies in Chinese");
	option[29] = $("<option>").val("H3-Economics").text("H3-Economics");
	option[30] = $("<option>").val("H3-Mathematics").text("H3-Mathematics");
	option[31] = $("<option>").val("Other").text("Other");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

function Option_ALEVEL_OTHER(s)
{
	$(s).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("H1-Bengali").text("H1-Bengali");
	option[2] = $("<option>").val("H1-Gujarati").text("H1-Gujarati");
	option[3] = $("<option>").val("H1-Hindi").text("H1-Hindi");
	option[4] = $("<option>").val("H1-French").text("H1-French");
	option[5] = $("<option>").val("H1-German").text("H1-German");
	option[6] = $("<option>").val("H1-Japanese").text("H1-Japanese");
	option[7] = $("<option>").val("H1-Panjabi").text("H1-Panjabi");
	option[8] = $("<option>").val("H1-Urdu").text("H1-Urdu");
	option[9] = $("<option>").val("H1-Malay Language").text("H1-Malay Language");
	option[10] = $("<option>").val("H1-Tamil Language").text("H1-Tamil Language");
	option[11] = $("<option>").val("H1-Art").text("H1-Art");
	option[12] = $("<option>").val("H2-Translation (Chinese)").text("H2-Translation (Chinese)");
	option[13] = $("<option>").val("H2-Theatre Studies and Drama").text("H2-Theatre Studies and Drama");
	option[14] = $("<option>").val("H2-English Language and Linguistics").text("H2-English Language and Linguistics");
	option[15] = $("<option>").val("H2-French").text("H2-French");
	option[16] = $("<option>").val("H2-German").text("H2-German");
	option[17] = $("<option>").val("H2-Japanese").text("H2-Japanese");
	option[18] = $("<option>").val("H2-Art").text("H2-Art");
	option[19] = $("<option>").val("H2-Music").text("H2-Music");
	option[20] = $("<option>").val("H2-Management of Business").text("H2-Management of Business");
	option[21] = $("<option>").val("H3-Literature in English").text("H3-Literature in English");
	option[22] = $("<option>").val("H3-Geography").text("H3-Geography");
	option[23] = $("<option>").val("H3-History").text("H3-History");
	option[24] = $("<option>").val("H3-Essentials of Modern Physics").text("H3-Essentials of Modern Physics");
	option[25] = $("<option>").val("H3-Pharmaceutical Chemistry").text("H3-Pharmaceutical Chemistry");
	option[26] = $("<option>").val("H3-Proteomics").text("H3-Proteomics");
	option[27] = $("<option>").val("H3-Art").text("H3-Art");
	option[28] = $("<option>").val("H3-Music").text("H3-Music");
	option[29] = $("<option>").val("H3-Chinese Language and Literature").text("H3-Chinese Language and Literature");
	
	
	for(i=0;i<option.length;i++)
	{
		$(s).append(option[i]);
	}
}

function Option_IB_MYP(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("Language Acquisition").text("Language Acquisition");
	option[2] = $("<option>").val("Economics").text("Economics");
	option[3] = $("<option>").val("Physical Sciences").text("Physical Sciences");
	option[4] = $("<option>").val("Standard Mathematics").text("Standard Mathematics");
	option[5] = $("<option>").val("Extended Mathematics").text("Extended Mathematics");
	option[6] = $("<option>").val("Other").text("Other");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

function Option_IB_MYP_OTHER(s)
{
	$(s).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("Language and Literature").text("Language and Literature");
	option[2] = $("<option>").val("Individuals and Societies").text("Individuals and Societies");
	option[3] = $("<option>").val("World, Local or National History").text("World, Local or National History");
	option[4] = $("<option>").val("Geography").text("geography");
	option[5] = $("<option>").val("Global Politics or International Relations").text("Global Politics or International Relations");
	option[6] = $("<option>").val("Civics").text("Civics");
	option[7] = $("<option>").val("Philosophy").text("Philosophy");
	option[8] = $("<option>").val("Business management").text("Business Management");
	option[9] = $("<option>").val("Sociology").text("Sociology");
	option[10] = $("<option>").val("Psychology").text("Psychology");
	option[11] = $("<option>").val("Anthropology").text("Anthropology");
	option[12] = $("<option>").val("Life Sciences").text("Life Sciences");
	option[13] = $("<option>").val("Health Sciences").text("Health Sciences");
	option[14] = $("<option>").val("Earth Sciences").text("Earth Sciences");
	
	for(i=0;i<option.length;i++)
	{
		$(s).append(option[i]);
	}
}

function Option_IB_DP(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("Theory of Knowledge").text("Theory of Knowledge");
	option[2] = $("<option>").val("Language A: Literature (SL/HL)").text("Language A: Literature (SL/HL)");
	option[3] = $("<option>").val("Language A: Language and Literature (SL/HL)").text("Language A: Language and Literature (SL/HL)");
	option[4] = $("<option>").val("Business Management (SL/HL)").text("Business Management (SL/HL)");
	option[5] = $("<option>").val("Economics (SL/HL)").text("Economics (SL/HL)");
	option[6] = $("<option>").val("Biology (SL/HL").text("Biology (SL/HL)");
	option[7] = $("<option>").val("Chemistry (SL/HL)").text("Chemistry (SL/HL)");
	option[8] = $("<option>").val("Physics (SL/HL").text("Physics (SL/HL)");
	option[9] = $("<option>").val("Mathematics (SL/HL)").text("Mathematics (SL/HL)");
	option[10] = $("<option>").val("Further Mathematics (HL)").text("Further Mathematics (HL)");
	option[11] = $("<option>").val("Other").text("Other");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

function Option_IB_DP_OTHER(s)
{
	$(s).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("The Extended Essay ").text("The Extended Essay ");
	option[2] = $("<option>").val("Creativity, Activity, Service").text("Creativity, Activity, Service");
	option[3] = $("<option>").val("Literature and Performance (SL)").text("Literature and Performance (SL)");
	option[4] = $("<option>").val("Geography (SL/HL)").text("Geography (SL/HL)");
	option[5] = $("<option>").val("Global Politics (SL/HL)").text("Global Politics (SL/HL)");
	option[6] = $("<option>").val("History (SL/HL)").text("History (SL/HL)");
	option[7] = $("<option>").val("Philosophy (SL/HL)").text("Philosophy (SL/HL)");
	option[8] = $("<option>").val("Psychology (SL/HL").text("Psychology (SL/HL)");
	option[9] = $("<option>").val("Computer Science (SL/HL)").text("Computer Science (SL/HL)");
	option[10] = $("<option>").val("Mathematical Studies Standard Level (SL/HL)").text("Mathematical Studies Standard Level (SL/HL)");
	
	for(i=0;i<option.length;i++)
	{
		$(s).append(option[i]);
	}
}

function Option_Zhongkao(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select subject");
	option[1] = $("<option>").val("Chinese").text("Chinese");
	option[2] = $("<option>").val("Mathematics").text("Mathematics");
	option[3] = $("<option>").val("English").text("English");
	option[4] = $("<option>").val("Physics").text("Physics");
	option[5] = $("<option>").val("Chemistry").text("Chemistry");
	option[6] = $("<option>").val("Biology").text("Biology");
	option[7] = $("<option>").val("History").text("History");
	option[8] = $("<option>").val("Geography").text("Geography");
	option[9] = $("<option>").val("Politics").text("Politics");
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
	option[1] = $("<option>").val("Chinese").text("Chinese");
	option[2] = $("<option>").val("Math").text("Math");
	option[3] = $("<option>").val("English").text("English");
	option[4] = $("<option>").val("Physics").text("Physics");
	option[5] = $("<option>").val("Vhemistry").text("Chemistry");
	option[6] = $("<option>").val("Biology").text("Biology");
	option[7] = $("<option>").val("History").text("History");
	option[8] = $("<option>").val("Geography").text("Geography");
	option[9] = $("<option>").val("Politics").text("Politics");
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
	option[1] = $("<option>").val("Chinese").text("Chinese");
	option[2] = $("<option>").val("Math").text("Math");
	option[3] = $("<option>").val("English").text("English");
	option[4] = $("<option>").val("???").text("???");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

function Option_Teaching_Level(s,n)
{
	$(s+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select teaching level");
	option[1] = $("<option>").val("PSLE").text("PSLE");
	option[2] = $("<option>").val("AEIS").text("AEIS");
	option[3] = $("<option>").val("O-LEVEL").text("O-LEVEL");
	option[4] = $("<option>").val("A-LEVEL").text("A-LEVEL");
	option[5] = $("<option>").val("IB(Middle Years Programme)").text("IB(Middle Years Programme)");
	option[6] = $("<option>").val("IB(Diploma Programme)").text("IB(Diploma Programme)");
	option[7] = $("<option>").val("Zhongkao").text("Zhongkao");
	option[8] = $("<option>").val("Gaokao").text("Gaokao");
	option[9] = $("<option>").val("SAT").text("SAT");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

function Option_Exam_Gaokao(n)
{
	$("#id_teaching_sub"+n).empty();
	var option = new Array();
	option[0] = $("<option>").val("").text("Select teaching subject");
	option[1] = $("<option>").val("Chinese").text("Chinese");
	option[2] = $("<option>").val("Math").text("Math");
	option[3] = $("<option>").val("English").text("English");
	option[4] = $("<option>").val("Combined Science").text("Combined Science");
	option[5] = $("<option>").val("Combined Art").text("Combined Art");
	for(i=0;i<option.length;i++)
	{
		$(s+n).append(option[i]);
	}
}

$(document).ready(function(){
									$("#btn_middle_test").hide();
									var num_middle_test = 0;
									$("#id_middle_test").change(function(){
																							for(i=0;i<num_middle_test;i++)
																							{
																							$("#num_middle_test").find(".row").eq(-1).remove();
																							$("#num_middle_test").find(".row").eq(-1).remove();
																							}
																							num_middle_test=0;
																							$("#btn_middle_test").hide();
																							if ($("#id_middle_test").val()!=""){
																							$("#btn_middle_test_add").click();
																							$("#btn_middle_test").show();
																							}
																							});
									$("#btn_middle_test_add").click(function(){
																									if ($("#id_middle_test").val()!="" && num_middle_test<9){
																									num_middle_test++;
																									$("#num_middle_test").append('<div class="row"> <div class="col-xs-4"> <div class="form-group"> <select class="form-control" id="id_middle_sub'+num_middle_test+'" name="middle_sub'+num_middle_test+'"> <option value="" selected="selected">Select subject</option> </select> </div></div> <div class="col-xs-4"> <div class="form-group"> <div id="num_middle_sub'+num_middle_test+'_other"> </div> </div></div></div>');
																									$("#num_middle_test").append('<div class="row"> <div class="col-xs-12"> <div class="form-group"> <input class="form-control" id="id_middle_sub'+num_middle_test+'_score" name="middle_sub'+num_middle_test+'_score" maxlength="50" name="one" type="text" placeholder="Score"/> </div> </div> </div>');
																									if ($("#id_middle_test").val()=="AEIS"){
																									Option_AEIS("#id_middle_sub",num_middle_test);
																									}
																									if ($("#id_middle_test").val()=="O-LEVEL"){
																									Option_OLEVEL("#id_middle_sub",num_middle_test);
																									}
																									if ($("#id_middle_test").val()=="IB(Middle Years Programme)"){
																									Option_IB_MYP("#id_middle_sub",num_middle_test);
																									}
																									if ($("#id_middle_test").val()=="Zhongkao"){
																									Option_Zhongkao("#id_middle_sub",num_middle_test);
																									}
																									
																									$("#id_middle_sub"+num_middle_test)
																									.change(function(){
																													s = this.name;
																													num = s[10];
																													
																													if ($(this).val()=="Other"){
																													$("#num_middle_sub"+num+"_other").empty();
																													$("#num_middle_sub"+num+"_other").append('<select class="form-control" id="id_middle_sub'+num+'_other" name="middle_sub'+num+'_other"> <option value="" selected="selected">Select subject</option> </select>');
																													if ($("#id_middle_test").val()=="O-LEVEL"){
																													Option_OLEVEL_OTHER("#id_middle_sub"+num+"_other");
																													}
																													if ($("#id_middle_test").val()=="IB(Middle Years Programme)"){
																													Option_IB_MYP_OTHER("#id_middle_sub"+num+"_other");
																													}
																													}
																													
																													
																													
																													});

																									
																									
																									
																									
																									}
																									});
									
									$("#btn_middle_test_remove").click(function(){
																										 if(num_middle_test>1){
																										 num_middle_test--;
																										 $("#num_middle_test").find(".row").eq(-1).remove();
																										 $("#num_middle_test").find(".row").eq(-1).remove();
																										 }
																										 });
									
									$("#btn_high_test").hide();
									var num_high_test = 0;
									$("#id_high_test").change(function(){
																							for(i=0;i<num_high_test;i++)
																							{
																							$("#num_high_test").find(".row").eq(-1).remove();
																							$("#num_high_test").find(".row").eq(-1).remove();
																							}
																							num_high_test=0;
																							$("#btn_high_test").hide();
																							if ($("#id_high_test").val()!=""){
																							$("#btn_high_test_add").click();
																							$("#btn_high_test").show();
																							}
																							});
									$("#btn_high_test_add").click(function(){
																									if ($("#id_high_test").val()!="" && num_high_test<9){
																									num_high_test++;
																									$("#num_high_test").append('<div class="row"> <div class="col-xs-4"> <div class="form-group"> <select class="form-control" id="id_high_sub'+num_high_test+'" name="high_sub'+num_high_test+'"> <option value="" selected="selected">Select subject</option> </select> </div></div> <div class="col-xs-4"> <div class="form-group"> <div id="num_high_sub'+num_high_test+'_other"> </div> </div></div></div>');
																									$("#num_high_test").append('<div class="row"> <div class="col-xs-12"> <div class="form-group"> <input class="form-control" id="id_high_sub'+num_high_test+'_score" name="high_sub'+num_high_test+'_score" maxlength="50" name="one" type="text" placeholder="Score"/> </div> </div> </div>');
																								if ($("#id_high_test").val()=="A-LEVEL"){
																								Option_ALEVEL("#id_high_sub",num_high_test);
																								}
																								if ($("#id_high_test").val()=="IB(Diploma Programme)"){
																								Option_IB_DP("#id_high_sub",num_high_test);
																								}
																								if ($("#id_high_test").val()=="Gaokao"){
																								Option_Gaokao("#id_high_sub",num_high_test);
																								}
																								if ($("#id_high_test").val()=="SAT"){
																								Option_SAT("#id_high_sub",num_high_test);
																								}
																									
																									$("#id_high_sub"+num_high_test)
																									.change(function(){
																													s = this.name;
																													num = s[8];
																													
																													if ($(this).val()=="Other"){
																													$("#num_high_sub"+num+"_other").empty();
																													$("#num_high_sub"+num+"_other").append('<select class="form-control" id="id_high_sub'+num+'_other" name="high_sub'+num+'_other"> <option value="" selected="selected">Select subject</option> </select>');
																													if ($("#id_high_test").val()=="A-LEVEL"){
																													Option_ALEVEL_OTHER("#id_high_sub"+num+"_other");
																													}
																													if ($("#id_high_test").val()=="IB(Diploma Programme)"){
																													Option_IB_DP_OTHER("#id_high_sub"+num+"_other");
																													}
																													}
																													
																													
																													
																													});
																									
																									
																									
																									
																									
																									}
																									});
									
									$("#btn_high_test_remove").click(function(){
																										 if(num_high_test>1){
																										 num_high_test--;
																										 $("#num_high_test").find(".row").eq(-1).remove();
																										 $("#num_high_test").find(".row").eq(-1).remove();
																										 }
																										 });
									
									
									
									
									var num_teaching_level = 1;
									$("#btn_teaching_level_add").click(function(){
																										 if(num_teaching_level<9){
																										 num_teaching_level++;
																										 $("#num_teaching_level").append('<div class="row"> <div class="col-xs-4"> <div class="form-group"> <select class="form-control" id="id_teaching_level'+num_teaching_level+'" name="teaching_level'+num_teaching_level+'"> <option value="" selected="selected">Select teaching level</option> </select> </div> </div> <div class="col-xs-4"> <div class="form-group"> <select class="form-control" id="id_teaching_sub'+num_teaching_level+'" name="teaching_sub'+num_teaching_level+'"> <option value="" selected="selected">Select subject</option> </select> </div> </div> <div id="id_teaching_other'+num_teaching_level+'" class="col-xs-4"> </div> </div>');
																										 Option_Teaching_Level( "#id_teaching_level",num_teaching_level);
																										 $("#id_teaching_level"+num_teaching_level)
																										 .change(function(){
																														 s = this.name;
																														 num = s[14];
																														 
																														$("#id_teaching_other"+num).empty();
																														if ($("#id_teaching_level"+num).val()=="")
																														 {
																														$("#id_teaching_sub"+num).empty();
																														var option = $("<option>").val("").text("Select subject");
																														$("#id_teaching_sub"+num).append(option);
																														 }
																
																														if ($("#id_teaching_level"+num).val()=="PSLE"){
																															Option_PSLE("#id_teaching_sub",num);
																																											}
																														if ($("#id_teaching_level"+num).val()=="AEIS"){
																																		Option_AEIS("#id_teaching_sub",num);
																																											}
																														if ($("#id_teaching_level"+num).val()=="O-LEVEL"){
																															Option_OLEVEL("#id_teaching_sub",num);
																																											}
																														if ($("#id_teaching_level"+num).val()=="A-LEVEL"){
																															Option_ALEVEL("#id_teaching_sub",num);
																																											}
																														if ($("#id_teaching_level"+num).val()=="IB(Middle Years Programme)"){
																															Option_IB_MYP("#id_teaching_sub",num);
																																											}
																														if ($("#id_teaching_level"+num).val()=="IB(Diploma Programme)"){
																																Option_IB_DP("#id_teaching_sub",num);
																																											}
																														if ($("#id_teaching_level"+num).val()=="Zhongkao"){
																																Option_Zhongkao("#id_teaching_sub",num);
																																											}
																														if ($("#id_teaching_level"+num).val()=="Gaokao"){
																																Option_Gaokao("#id_teaching_sub",num);
																																											}
																														if ($("#id_teaching_level"+num).val()=="SAT"){
																																Option_SAT("#id_teaching_sub",num);
																																											}
																																											});
																										 
																										 $("#id_teaching_sub"+num_teaching_level)
																										 .change(function(){
																														 s = this.name;
																														 num = s[12];
																														 
																														 if ($(this).val()=="Other"){
																														 $("#id_teaching_other"+num).empty();
																														 $("#id_teaching_other"+num).append('<div class="form-group"> <select class="form-control" id="id_teaching_sub'+num+'_other" name="teaching_sub'+num+'_other"> <option value="" selected="selected">Select subject</option> </select> </div>');
																														 if ($("#id_teaching_level"+num).val()=="O-LEVEL"){
																														 Option_OLEVEL_OTHER("#id_teaching_sub"+num+"_other");
																														 }
																														 if ($("#id_teaching_level"+num).val()=="A-LEVEL"){
																														 Option_ALEVEL_OTHER("#id_teaching_sub"+num+"_other");
																														 }
																														 if ($("#id_teaching_level"+num).val()=="IB(Middle Years Programme)"){
																														 Option_IB_MYP_OTHER("#id_teaching_sub"+num+"_other");
																														 }
																														 if ($("#id_teaching_level"+num).val()=="IB(Diploma Programme)"){
																														 Option_IB_DP_OTHER("#id_teaching_sub"+num+"_other");
																														 }
																														 }
																														 });
																										 
																										 }
																								});
									
									$("#btn_teaching_level_remove").click(function(){
																											 if(num_teaching_level>1){
																											 num_teaching_level--;
																											 $("#num_teaching_level").find(".row").eq(-1).remove();
																											 }
																											 });
									
									$("#id_teaching_level1").change(function(){
																									 $("#id_teaching_other1").empty();
																									 if ($("#id_teaching_level1").val()==""){
																									 $("#id_teaching_sub1").empty();
																									 var option = $("<option>").val("").text("Select subject");
																									 $("#id_teaching_sub1").append(option);
																									 }
																									 if ($("#id_teaching_level1").val()=="PSLE"){
																									 Option_PSLE("#id_teaching_sub",1);
																									 }
																									 if ($("#id_teaching_level1").val()=="AEIS"){
																									 Option_AEIS("#id_teaching_sub",1);
																									 }
																									 if ($("#id_teaching_level1").val()=="O-LEVEL"){
																									 Option_OLEVEL("#id_teaching_sub",1);
																									 }
																									 if ($("#id_teaching_level1").val()=="A-LEVEL"){
																									 Option_ALEVEL("#id_teaching_sub",1);
																									 }
																									 if ($("#id_teaching_level1").val()=="IB(Middle Years Programme)"){
																									 Option_IB_MYP("#id_teaching_sub",1);
																									 }
																									 if ($("#id_teaching_level1").val()=="IB(Diploma Programme)"){
																									 Option_IB_DP("#id_teaching_sub",1);
																									 }
																									 if ($("#id_teaching_level1").val()=="Zhongkao"){
																									 Option_Zhongkao("#id_teaching_sub",1);
																									 }
																									 if ($("#id_teaching_level1").val()=="Gaokao"){
																									 Option_Gaokao("#id_teaching_sub",1);
																									 }
																									 if ($("#id_teaching_level1").val()=="SAT"){
																									 Option_SAT("#id_teaching_sub",1);
																									 }
																									 });
									$("#id_teaching_sub1").change(function(){
																								if ($(this).val()=="Other"){
																								$("#id_teaching_other1").empty();
																								$("#id_teaching_other1").append('<div class="form-group"> <select class="form-control" id="id_teaching_sub1_other" name="teaching_sub1_other"> <option value="" selected="selected">Select subject</option> </select> </div>');
																								
																								if ($("#id_teaching_level1").val()=="O-LEVEL"){
																								Option_OLEVEL_OTHER("#id_teaching_sub1_other");
																								}
																								if ($("#id_teaching_level1").val()=="A-LEVEL"){
																								Option_ALEVEL_OTHER("#id_teaching_sub1_other");
																								}
																								if ($("#id_teaching_level1").val()=="IB(Middle Years Programme)"){
																								Option_IB_MYP_OTHER("#id_teaching_sub1_other");
																								}
																								if ($("#id_teaching_level1").val()=="IB(Diploma Programme)"){
																								Option_IB_DP_OTHER("#id_teaching_sub1_other");
																								}
																								}
			
																								
																								});

									



									
									
                  });




