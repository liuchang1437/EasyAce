var count_prefer = 0;
function add_prefer()
{

	if(count_prefer<9){
		count_prefer++;
		temp =  '<div class="row" style="margin-top:20px">'
		temp += '<h2 style="color: #759049; font-size: 20px;">preference '+count_prefer+'</h2>';
		temp += '<div class="col-xs-6">';
		temp += '<div class="col-xs-12 form-group">';
		temp += '<select class="form-control" id="id_teach_level'+count_prefer+'" name="teach_level'+count_prefer+'">';
		temp += '<option value="" selected="selected">Select level</option> </select> </div>'
		temp += '<div class="col-xs-12 form-group">';
		temp += '<select class="form-control" id="id_teach_sub'+count_prefer+'" name="teach_sub'+count_prefer+'">';
		temp += '<option value="" selected="selected">Select subject</option> </select> </div>';
		temp += '<div class="col-xs-12 form-group">';
		temp += '<select class="form-control" id="id_teach_sub_other'+count_prefer+'" name="teach_sub_other'+count_prefer+'">';
		temp += '<option value="" selected="selected">Select subject</option> </select> </div>';
		temp += '</div> <div class="col-xs-6">';
		temp += '<div class="col-xs-12 form-group">';
		temp += '<select class="form-control" id="id_ref_level'+count_prefer+'" name="ref_level'+count_prefer+'">';
		temp += '<option value="" selected="selected">Select level</option> </select> </div>';
		temp += '<div class="col-xs-12 form-group">';
		temp += '<select class="form-control" id="id_ref_sub'+count_prefer+'" name="ref_sub'+count_prefer+'">';
		temp += '<option value="" selected="selected">Select subject</option> </select> </div>';
		temp += '<div class="col-xs-12 form-group" id="block_ref_sub_other'+count_prefer+'">';
		temp += '<select class="form-control" id="id_ref_sub_other'+count_prefer+'" name="ref_sub_other'+count_prefer+'">';
		temp += '<option value="" selected="selected">Select subject</option> </select> </div>';
		temp += '<div class="col-xs-12 form-group">';
		temp += '<select class="form-control" id="id_ref_score'+count_prefer+'" name="ref_score'+count_prefer+'">';
		temp += '<option value="" selected="selected">Select score</option> </select> </div>';
		temp += '</div></div> ';
		$("#block_prefer").append(temp);
		$("#id_teach_sub_other"+count_prefer).hide();
		$("#block_ref_sub_other"+count_prefer).hide();

		Option_Teaching_Level( "#id_teach_level",count_prefer);
		$("#id_teach_level"+count_prefer).change(function(){
 			s = this.name;
 			num = s[11];
 
			$("#id_teach_sub_other"+num).hide();
			if ($("#id_teach_level"+num).val()=="")
 			{
				$("#id_teach_sub"+num).empty();
				var option = $("<option>").val("").text("Select subject");
				$("#id_teach_sub"+num).append(option);
 			}

			if ($("#id_teach_level"+num).val()=="PSLE"){
				Option_PSLE("#id_teach_sub",num);
			}
			if ($("#id_teach_level"+num).val()=="AEIS"){
				Option_AEIS("#id_teach_sub",num);
			}
			if ($("#id_teach_level"+num).val()=="O-LEVEL"){
				Option_OLEVEL("#id_teach_sub",num);
			}
			if ($("#id_teach_level"+num).val()=="A-LEVEL"){
				Option_ALEVEL("#id_teach_sub",num);
			}
			if ($("#id_teach_level"+num).val()=="IB (Middle Years Programme)"){
				Option_IB_MYP("#id_teach_sub",num);
			}
			if ($("#id_teach_level"+num).val()=="IB (Diploma Programme)"){
				Option_IB_DP("#id_teach_sub",num);
			}
			if ($("#id_teach_level"+num).val()=="Zhongkao"){
				Option_Zhongkao("#id_teach_sub",num);
			}
			if ($("#id_teach_level"+num).val()=="Gaokao"){
				Option_Gaokao("#id_teach_sub",num);
			}
			if ($("#id_teach_level"+num).val()=="SAT"){
				Option_SAT("#id_teach_sub",num);
			}
		});

		$("#id_teach_sub"+count_prefer).change(function(){
			s = this.name;
			num = s[9];
			 
			if ($(this).val()=="Other"){
				$("#id_teach_sub_other"+num).show();
				$("#id_teach_sub_other"+num).empty();
				if ($("#id_teach_level"+num).val()=="O-LEVEL"){
					Option_OLEVEL_OTHER("#id_teach_sub_other"+num);
				}
				if ($("#id_teach_level"+num).val()=="A-LEVEL"){
					Option_ALEVEL_OTHER("#id_teach_sub_other"+num);
				}
				if ($("#id_teach_level"+num).val()=="IB (Middle Years Programme)"){
					Option_IB_MYP_OTHER("#id_teach_sub_other"+num);
				}
				if ($("#id_teach_level"+num).val()=="IB (Diploma Programme)"){
					Option_IB_DP_OTHER("#id_teach_sub_other"+num);
				}
			}
		});

////////////////////////////////reference//////////////////////////////////////////////

		Option_ref_Level( "#id_ref_level",count_prefer);
		$("#id_ref_level"+count_prefer).change(function(){
 			s = this.name;
 			num = s[9];
 
			$("#block_ref_sub_other"+num).hide();
			if ($("#id_ref_level"+num).val()=="")
 			{
				$("#id_ref_sub"+num).empty();
				var option = $("<option>").val("").text("Select subject");
				$("#id_ref_sub"+num).append(option);
 			}

			if ($("#id_ref_level"+num).val()=="O-LEVEL"){
				Option_OLEVEL("#id_ref_sub",num);
				Option_score("O-LEVEL","#id_ref_score"+num);
			}
			if ($("#id_ref_level"+num).val()=="A-LEVEL"){
				Option_ALEVEL("#id_ref_sub",num);
				Option_score("A-LEVEL","#id_ref_score"+num);
			}
			if ($("#id_ref_level"+num).val()=="IB (Middle Years Programme)"){
				Option_IB_MYP("#id_ref_sub",num);
				Option_score("IB (Middle Years Programme)","#id_ref_score"+num);
			}
			if ($("#id_ref_level"+num).val()=="IB (Diploma Programme)"){
				Option_IB_DP("#id_ref_sub",num);
				Option_score("IB (Diploma Programme)","#id_ref_score"+num);
			}
			if ($("#id_ref_level"+num).val()=="Zhongkao"){
				Option_Zhongkao("#id_ref_sub",num);
				Option_score("Zhongkao","#id_ref_score"+num);
			}
			if ($("#id_ref_level"+num).val()=="Gaokao"){
				Option_Gaokao("#id_ref_sub",num);
				Option_score("Gaokao","#id_ref_score"+num);
			}
			if ($("#id_ref_level"+num).val()=="SAT"){
				Option_SAT("#id_ref_sub",num);
			}
		});

		$("#id_ref_sub"+count_prefer).change(function(){
			s = this.name;
			num = s[7];
			 
			if ($(this).val()=="Other"){
				$("#block_ref_sub_other"+num).show();
				$("#id_ref_sub_other"+num).empty();
				if ($("#id_ref_level"+num).val()=="O-LEVEL"){
					Option_OLEVEL_OTHER("#id_ref_sub_other"+num);
				}
				if ($("#id_ref_level"+num).val()=="A-LEVEL"){
					Option_ALEVEL_OTHER("#id_ref_sub_other"+num);
				}
				if ($("#id_ref_level"+num).val()=="IB (Middle Years Programme)"){
					Option_IB_MYP_OTHER("#id_ref_sub_other"+num);
				}
				if ($("#id_ref_level"+num).val()=="IB (Diploma Programme)"){
					Option_IB_DP_OTHER("#id_ref_sub_other"+num);
				}
			}
		});



	}
}

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
	add_prefer();

	$("#btn_prefer_add").click(function(){
		add_prefer();
		
	});

	$("#btn_prefer_remove").click(function(){
		if(count_prefer>1){
			count_prefer--;
			$("#block_prefer").find(".row").eq(-1).remove();
		}
	});

});




