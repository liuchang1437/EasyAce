var num_teaching_level = 1;
function add_prefer()
{
	if(num_teaching_level<9){
		num_teaching_level++;
		$("#num_teaching_level").append('<div class="row"> <div class="col-xs-4"> <div class="form-group"> <select class="form-control" id="id_teaching_level'+num_teaching_level+'" name="teaching_level'+num_teaching_level+'"> <option value="" selected="selected">Select teaching level</option> </select> </div> </div> <div class="col-xs-4"> <div class="form-group"> <select class="form-control" id="id_teaching_sub'+num_teaching_level+'" name="teaching_sub'+num_teaching_level+'"> <option value="" selected="selected">Select subject</option> </select> </div> </div> <div id="id_teaching_other'+num_teaching_level+'" class="col-xs-4"> </div> </div>');
		Option_Teaching_Level( "#id_teaching_level",num_teaching_level);
		$("#id_teaching_level"+num_teaching_level).change(function(){
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
			if ($("#id_teaching_level"+num).val()=="IB (Middle Years Programme)"){
				Option_IB_MYP("#id_teaching_sub",num);
			}
			if ($("#id_teaching_level"+num).val()=="IB (Diploma Programme)"){
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

		$("#id_teaching_sub"+num_teaching_level).change(function(){
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
				if ($("#id_teaching_level"+num).val()=="IB (Middle Years Programme)"){
					Option_IB_MYP_OTHER("#id_teaching_sub"+num+"_other");
				}
				if ($("#id_teaching_level"+num).val()=="IB (Diploma Programme)"){
					Option_IB_DP_OTHER("#id_teaching_sub"+num+"_other");
				}
			}
		});
	}
}

var num_middle_test = 0;
function add_middle()
{
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
		if ($("#id_middle_test").val()=="IB (Middle Years Programme)"){
			Option_IB_MYP("#id_middle_sub",num_middle_test);
		}
		if ($("#id_middle_test").val()=="Zhongkao"){
			Option_Zhongkao("#id_middle_sub",num_middle_test);
		}
		$("#id_middle_sub"+num_middle_test).change(function(){
			s = this.name;
			num = s[10];
			if ($(this).val()=="Other"){
				$("#num_middle_sub"+num+"_other").empty();
				$("#num_middle_sub"+num+"_other").append('<select class="form-control" id="id_middle_sub'+num+'_other" name="middle_sub'+num+'_other"> <option value="" selected="selected">Select subject</option> </select>');
				if ($("#id_middle_test").val()=="O-LEVEL"){
					Option_OLEVEL_OTHER("#id_middle_sub"+num+"_other");
				}
				if ($("#id_middle_test").val()=="IB (Middle Years Programme)"){
					Option_IB_MYP_OTHER("#id_middle_sub"+num+"_other");
				}
			}
		});
	}
}
var num_high_test = 0;
function add_high()
{
	if ($("#id_high_test").val()!="" && num_high_test<9){
		num_high_test++;
		$("#num_high_test").append('<div class="row"> <div class="col-xs-4"> <div class="form-group"> <select class="form-control" id="id_high_sub'+num_high_test+'" name="high_sub'+num_high_test+'"> <option value="" selected="selected">Select subject</option> </select> </div></div> <div class="col-xs-4"> <div class="form-group"> <div id="num_high_sub'+num_high_test+'_other"> </div> </div></div></div>');
		$("#num_high_test").append('<div class="row"> <div class="col-xs-12"> <div class="form-group"> <input class="form-control" id="id_high_sub'+num_high_test+'_score" name="high_sub'+num_high_test+'_score" maxlength="50" name="one" type="text" placeholder="Score"/> </div> </div> </div>');
		if ($("#id_high_test").val()=="A-LEVEL"){
			Option_ALEVEL("#id_high_sub",num_high_test);
		}
		if ($("#id_high_test").val()=="IB (Diploma Programme)"){
			Option_IB_DP("#id_high_sub",num_high_test);
		}
		if ($("#id_high_test").val()=="Gaokao"){
			Option_Gaokao("#id_high_sub",num_high_test);
		}
		if ($("#id_high_test").val()=="SAT"){
			Option_SAT("#id_high_sub",num_high_test);
		}
		$("#id_high_sub"+num_high_test).change(function(){
			s = this.name;
			num = s[8];

			if ($(this).val()=="Other"){
				$("#num_high_sub"+num+"_other").empty();
				$("#num_high_sub"+num+"_other").append('<select class="form-control" id="id_high_sub'+num+'_other" name="high_sub'+num+'_other"> <option value="" selected="selected">Select subject</option> </select>');
				if ($("#id_high_test").val()=="A-LEVEL"){
					Option_ALEVEL_OTHER("#id_high_sub"+num+"_other");
				}
				if ($("#id_high_test").val()=="IB (Diploma Programme)"){
					Option_IB_DP_OTHER("#id_high_sub"+num+"_other");
				}
			}
		});
	}
}

var middle_test = "";
var high_test = "";
//var middle_subjects,high_subjects,prefer_tests,middle_subjects_other,high_subjects_other,prefer_tests_other = new Array();
//var middle_scores,high_scores,prefer_subjects,middle_scores_other,high_scores_other,prefer_subjects_other = new Array();
var middle_subjects = [];
var middle_subjects_other = [];
var middle_scores = [];
var high_subjects = [];
var high_subjects_other = [];
var high_scores = [];
var prefer_tests = [];
var prefer_subjects = []
var prefer_subjects_other = []
var num_middle,num_high,num_prefer;
var edit = false;
function get_subjects()
{
	$.ajax({url:"/edit_tutor/",
			type:"post",
			async:false,
			datatype:"text",
			success: function(data){
				edit = true;
				obj = jQuery.parseJSON(data);
				middle_test = obj["middle_test"];
				high_test = obj["high_test"];
				num_middle = 0;
				num_high = 0;
				num_prefer = 0;
				for(sub in obj["middle_test_score"])
					if( sub != "Other")
					{
						num_middle += 1;
						middle_subjects[num_middle] = sub;
						middle_scores[num_middle] = obj["middle_test_score"][sub];
					}
				for(i=0;i<obj["middle_sub_other"].length;i++)
				{
					num_middle += 1;
					middle_subjects[num_middle] = "Other";
					middle_subjects_other[num_middle] = obj["middle_sub_other"][i][1];
					middle_scores[num_middle] = obj["middle_sub_other"][i][2];
				}
				for(sub in obj["high_test_score"])
					if( sub != "Other")
					{
						num_high += 1;
						high_subjects[num_high] = sub;
						high_scores[num_high] = obj["high_test_score"][sub];
					}
				for(i=0;i<obj["high_sub_other"].length;i++)
				{
					num_high += 1;
					high_subjects[num_high] = "Other";
					high_subjects_other[num_high] = obj["high_sub_other"][i][1];
					high_scores[num_high] = obj["high_sub_other"][i][2];

				}
				num_prefer = 0;
				count = 0;
				for(i=0;i<obj["prefer_teach"].length;i++)
					if(obj["prefer_teach"][i][0] != "Other")
					{
						num_prefer += 1;
						prefer_tests[num_prefer] = obj["prefer_teach"][i][0];
						prefer_subjects[num_prefer] = obj["prefer_teach"][i][1];
						if(prefer_subjects[num_prefer] == "Other")
						{
							prefer_subjects_other[num_prefer] = obj["teaching_sub_other"][count][2];
							count += 1;
						}
					}
			},
			error: function(){
			}

		});
	//middle test
	if(num_middle > 0)
	{
		doc = document.getElementById("id_middle_test");
		for(j=0;j<doc.length;j++)
			if(doc.options[j].text == middle_test)
			{
				doc.selectedIndex = j;
				break;
			}
		$("#btn_middle_test").show();
		count = 1;
		for(i=0;i<num_middle;i++)
		{
			now = i + 1;
			add_middle();
			doc = document.getElementById("id_middle_sub" + now);
			other = false;
			for(j=0;j<doc.length;j++)
				if(doc.options[j].text == middle_subjects[now])
				{
					doc.selectedIndex = j;
					if(middle_subjects[now] == "Other") 
						other = true;
					break;
				}
			if(other)
			{
				$("#num_middle_sub"+now+"_other").append('<select class="form-control" id="id_middle_sub'+now+'_other" name="middle_sub'+now+'_other"> <option value="" selected="selected">Select subject</option> </select>');
				if ($("#id_middle_test").val()=="O-LEVEL"){
					Option_OLEVEL_OTHER("#id_middle_sub"+now+"_other");
				}
				if ($("#id_middle_test").val()=="A-LEVEL"){
					Option_ALEVEL_OTHER("#id_middle_sub"+now+"_other");
				}
				if ($("#id_middle_test").val()=="IB (Middle Years Programme)"){
					Option_IB_MYP_OTHER("#id_middle_sub"+now+"_other");
				}
				if ($("#id_middle_test").val()=="IB (Diploma Programme)"){
					Option_IB_DP_OTHER("#id_middle_sub"+now+"_other");
				}
				doc = document.getElementById("id_middle_sub" + now + "_other");
				for(j=0;j<doc.length;j++)
					if(doc.options[j].text == middle_subjects_other[now])
					{
						doc.selectedIndex = j;
						break;
					}
			}
			doc = document.getElementById("id_middle_sub" + now + "_score");
			doc.value = middle_scores[now];
			i = now - 1;
		}
	}

	//high test
	if(num_high > 0)
	{
		doc = document.getElementById("id_high_test");
		for(j=0;j<doc.length;j++)
			if(doc.options[j].text == high_test)
			{
				doc.selectedIndex = j;
				break;
			}
		$("#btn_high_test").show();
		for(i=0;i<num_high;i++)
		{
			now = i + 1;
			add_high();
			doc = document.getElementById("id_high_sub" + now);
			other = false;
			for(j=0;j<doc.length;j++)
				if(doc.options[j].text == high_subjects[now])
				{
					doc.selectedIndex = j;
					if(high_subjects[now] == "Other") 
						other = true;
					break;
				}
			if(other)
			{
				$("#num_high_sub"+now+"_other").append('<select class="form-control" id="id_high_sub'+now+'_other" name="high_sub'+now+'_other"> <option value="" selected="selected">Select subject</option> </select>');
				if ($("#id_high_test").val()=="O-LEVEL"){
					Option_OLEVEL_OTHER("#id_high_sub"+now+"_other");
				}
				if ($("#id_high_test").val()=="A-LEVEL"){
					Option_ALEVEL_OTHER("#id_high_sub"+now+"_other");
				}
				if ($("#id_high_test").val()=="IB (high Years Programme)"){
					Option_IB_MYP_OTHER("#id_high_sub"+now+"_other");
				}
				if ($("#id_high_test").val()=="IB (Diploma Programme)"){
					Option_IB_DP_OTHER("#id_high_sub"+now+"_other");
				}
				doc = document.getElementById("id_high_sub" + now + "_other");
				for(j=0;j<doc.length;j++)
					if(doc.options[j].text == high_subjects_other[now])
					{
						doc.selectedIndex = j;
						break;
					}
			}
			doc = document.getElementById("id_high_sub" + now + "_score");
			doc.value = high_scores[now];
			i = now - 1;
		}
	}

	if(num_prefer > 0)
	{
		doc = document.getElementById("id_teaching_level1");
		for(j=0;j<doc.length;j++)
			if(doc.options[j].text == prefer_tests[1])
			{
				doc.selectedIndex = j;
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
				if ($("#id_teaching_level1").val()=="IB (Middle Years Programme)"){
					Option_IB_MYP("#id_teaching_sub",1);
				}
				if ($("#id_teaching_level1").val()=="IB (Diploma Programme)"){
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
				break;
			}
		doc = document.getElementById("id_teaching_sub1");
		other = false
		for(j=0;j<doc.length;j++)
			if(doc.options[j].text == prefer_subjects[1])
			{
				doc.selectedIndex = j;
				if(prefer_subjects[1] == "Other") 
					other = true;
				break;
			}
		if(other)
		{
			$("#id_teaching_other1").append('<div class="form-group"> <select class="form-control" id="id_teaching_sub1_other" name="teaching_sub1_other"> <option value="" selected="selected">Select subject</option> </select> </div>');
				if ($("#id_teaching_level1").val()=="O-LEVEL"){
					Option_OLEVEL_OTHER("#id_teaching_sub1_other");
				}
				if ($("#id_teaching_level1").val()=="A-LEVEL"){
					Option_ALEVEL_OTHER("#id_teaching_sub1_other");
				}
				if ($("#id_teaching_level1").val()=="IB (Middle Years Programme)"){
					Option_IB_MYP_OTHER("#id_teaching_sub1_other");
				}
				if ($("#id_teaching_level1").val()=="IB (Diploma Programme)"){
					Option_IB_DP_OTHER("#id_teaching_sub1_other");
				}
				doc = document.getElementById("id_teaching_sub1_other");
				for(j=0;j<doc.length;j++)
					if(doc.options[j].text == prefer_subjects_other[1])
					{
						doc.selectedIndex = j;
						break;
					}
		}


		for(i=1;i<num_prefer;i++)
		{
			now = i + 1;
			add_prefer();
			doc = document.getElementById("id_teaching_level" + now);
			for(j=0;j<doc.length;j++)
				if(doc.options[j].text == prefer_tests[now])
				{
					doc.selectedIndex = j;
					if ($("#id_teaching_level"+now).val()=="PSLE"){
						Option_PSLE("#id_teaching_sub",now);
					}
					if ($("#id_teaching_level"+now).val()=="AEIS"){
						Option_AEIS("#id_teaching_sub",now);
					}
					if ($("#id_teaching_level"+now).val()=="O-LEVEL"){
						Option_OLEVEL("#id_teaching_sub",now);
					}
					if ($("#id_teaching_level"+now).val()=="A-LEVEL"){
						Option_ALEVEL("#id_teaching_sub",now);
					}
					if ($("#id_teaching_level"+now).val()=="IB (Middle Years Programme)"){
						Option_IB_MYP("#id_teaching_sub",now);
					}
					if ($("#id_teaching_level"+now).val()=="IB (Diploma Programme)"){
						Option_IB_DP("#id_teaching_sub",now);
					}
					if ($("#id_teaching_level"+now).val()=="Zhongkao"){
						Option_Zhongkao("#id_teaching_sub",now);
					}
					if ($("#id_teaching_level"+now).val()=="Gaokao"){
						Option_Gaokao("#id_teaching_sub",now);
					}
					if ($("#id_teaching_level"+now).val()=="SAT"){
						Option_SAT("#id_teaching_sub",now);
					}
					break;
				}
			doc = document.getElementById("id_teaching_sub" + now);
			other = false;
			for(j=0;j<doc.length;j++)
				if(doc.options[j].text == prefer_subjects[now])
				{
					doc.selectedIndex = j;
					if(prefer_subjects[now] == "Other") 
						other = true;
					break;
				}
			if(other)
			{
				$("#id_teaching_other"+now).append('<div class="form-group"> <select class="form-control" id="id_teaching_sub'+now+'_other" name="teaching_sub'+now+'_other"> <option value="" selected="selected">Select subject</option> </select> </div>');
				if ($("#id_teaching_level"+now).val()=="O-LEVEL"){
					Option_OLEVEL_OTHER("#id_teaching_sub"+now+"_other");
				}
				if ($("#id_teaching_level"+now).val()=="A-LEVEL"){
					Option_ALEVEL_OTHER("#id_teaching_sub"+now+"_other");
				}
				if ($("#id_teaching_level"+now).val()=="IB (Middle Years Programme)"){
					Option_IB_MYP_OTHER("#id_teaching_sub"+now+"_other");
				}
				if ($("#id_teaching_level"+now).val()=="IB (Diploma Programme)"){
					Option_IB_DP_OTHER("#id_teaching_sub"+now+"_other");
				}
				doc = document.getElementById("id_teaching_sub" + now + "_other");
				for(j=0;j<doc.length;j++)
					if(doc.options[j].text == prefer_subjects_other[now])
					{
						doc.selectedIndex = j;
						break;
					}
			}
			i = now - 1;
		}
	}


}

$(document).ready(function(){
	$("#btn_middle_test").hide();
	get_subjects();
									
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
		add_middle();
	});

	$("#btn_middle_test_remove").click(function(){
		if(num_middle_test>1){
			num_middle_test--;
			$("#num_middle_test").find(".row").eq(-1).remove();
			$("#num_middle_test").find(".row").eq(-1).remove();
		}
	});

	$("#btn_high_test").hide();
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
			add_high();
		});

	$("#btn_high_test_remove").click(function(){
		if(num_high_test>1){
			num_high_test--;
			$("#num_high_test").find(".row").eq(-1).remove();
			$("#num_high_test").find(".row").eq(-1).remove();
		}
	});

	$("#btn_teaching_level_add").click(function(){
		add_prefer();
		
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
		if ($("#id_teaching_level1").val()=="IB (Middle Years Programme)"){
			Option_IB_MYP("#id_teaching_sub",1);
		}
		if ($("#id_teaching_level1").val()=="IB (Diploma Programme)"){
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
			if ($("#id_teaching_level1").val()=="IB (Middle Years Programme)"){
				Option_IB_MYP_OTHER("#id_teaching_sub1_other");
			}
			if ($("#id_teaching_level1").val()=="IB (Diploma Programme)"){
				Option_IB_DP_OTHER("#id_teaching_sub1_other");
			}
		}
	});
});




