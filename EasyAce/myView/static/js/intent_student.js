function add_subject()
{
	if ($("#id_student_subject").val()!="" && num_student_subject<9){
		num_student_subject++;
		$("#num_student_subject").append('<div class="row"> <div class="col-xs-6"> <div class="form-group"> <select class="form-control" id="id_student_subject'+num_student_subject+'" name="student_subject'+num_student_subject+'"> <option value="" selected="selected">Select subject</option> </select> </div></div> <div id="num_student_subject_other'+num_student_subject+'"></div> </div>');
		
		$("#id_student_subject"+num_student_subject).change(function (){
			s = this.name;
			num = s[15];
			$("#num_student_subject_other"+num).empty();
			if ($(this).val()=="Other"){
				var qwe = 0;
				$("#num_student_subject_other"+num).append('<div class="col-xs-6"> <div class="form-group"> <select class="form-control" id="id_student_subject'+num+'_other" name="student_subject'+num+'_other"> <option value="" selected="selected">Select subject</option> </div> </div>');
			}
																									
			if ($("#id_student_subject").val()=="O-LEVEL"){
				Option_OLEVEL_OTHER("#id_student_subject"+num+"_other");
			}
			if ($("#id_student_subject").val()=="A-LEVEL"){
				Option_ALEVEL_OTHER("#id_student_subject"+num+"_other");
			}
			if ($("#id_student_subject").val()=="IB (Middle Years Programme)"){
				Option_IB_MYP_OTHER("#id_student_subject"+num+"_other");
			}
			if ($("#id_student_subject").val()=="IB (Diploma Programme)"){
				Option_IB_DP_OTHER("#id_student_subject"+num+"_other");
			}
		});
		if ($("#id_student_subject").val()=="PSLE"){
			Option_PSLE("#id_student_subject",num_student_subject);
		}
		if ($("#id_student_subject").val()=="AEIS"){
			Option_AEIS("#id_student_subject",num_student_subject);
		}
		if ($("#id_student_subject").val()=="O-LEVEL"){
			Option_OLEVEL("#id_student_subject",num_student_subject);
		}
		if ($("#id_student_subject").val()=="A-LEVEL"){
			Option_ALEVEL("#id_student_subject",num_student_subject);
		}
		if ($("#id_student_subject").val()=="IB (Middle Years Programme)"){
			Option_IB_MYP("#id_student_subject",num_student_subject);
		}
		if ($("#id_student_subject").val()=="IB (Diploma Programme)"){
			Option_IB_DP("#id_student_subject",num_student_subject);
		}
		if ($("#id_student_subject").val()=="Zhongkao"){
			Option_Zhongkao("#id_student_subject",num_student_subject);
		}
		if ($("#id_student_subject").val()=="Gaokao"){
			Option_Gaokao("#id_student_subject",num_student_subject);
		}
		if ($("#id_student_subject").val()=="SAT"){
			Option_SAT("#id_student_subject",num_student_subject);
		}
	}
}
var subjects = new Array();
var subjects_other = new Array();
var num_subjects = 0;
var exam_type = "";
var edit = false;
function get_subjects()
{
	$.ajax({url:"/edit_student/",
			type:"post",
			async:false,
			datatype:"text",
			success: function(data){
				obj = jQuery.parseJSON(data);
				exam_type = obj["exam_type"];
				num_subjects = obj["subjects"].length;
				for(i=0;i<num_subjects;i++)
				{
					edit = true;
					subjects[i] = obj["subjects"][i];
					subjects_other[i] = obj["subjects_other"][i];
				}
			},
			error: function(){
			}

		});
	if(num_subjects > 0)
	{
		$("#btn_student_subject").show();
		for(i=0;i<num_subjects;i++)
		{
			now = i + 1;
			doc = document.getElementById("id_student_subject");
			for(j=0;j<doc.length;j++)
				if(doc.options[j].text == exam_type)
				{
					doc.selectedIndex = j;
					break;
				}
			add_subject();
			doc = document.getElementById("id_student_subject" + now);
			other = false;
			if(subjects_other[now-1])
			{
				doc.selectedIndex = doc.length - 1;
				other = true;
			}
			else
				for(j=0;j<doc.length;j++)
					if(doc.options[j].text == subjects[now-1])
					{
						doc.selectedIndex = j;
						break;
					}
			if(other)
			{
				$("#num_student_subject_other"+now).append('<div class="col-xs-6"> <div class="form-group"> <select class="form-control" id="id_student_subject'+now+'_other" name="student_subject'+now+'_other"> <option value="" selected="selected">Select subject</option> </div> </div>');
				if ($("#id_student_subject").val()=="O-LEVEL"){
					Option_OLEVEL_OTHER("#id_student_subject"+now+"_other");
				}
				if ($("#id_student_subject").val()=="A-LEVEL"){
					Option_ALEVEL_OTHER("#id_student_subject"+now+"_other");
				}
				if ($("#id_student_subject").val()=="IB (Middle Years Programme)"){
					Option_IB_MYP_OTHER("#id_student_subject"+now+"_other");
				}
				if ($("#id_student_subject").val()=="IB (Diploma Programme)"){
					Option_IB_DP_OTHER("#id_student_subject"+now+"_other");
				}
				doc = document.getElementById("id_student_subject" + now + "_other");
				for(j=0;j<doc.length;j++)
					if(doc.options[j].text == subjects[now-1])
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
	$("#id_intent_subject_other").hide();

	$("#id_intent_level").change(function(){
		$("#id_intent_subject_other").hide();

		if ($("#id_intent_level").val()=="PSLE"){
			Option_PSLE("#id_intent_subject","");
		}
		if ($("#id_intent_level").val()=="O-LEVEL"){
			Option_OLEVEL("#id_intent_subject","");
		}
		if ($("#id_intent_level").val()=="A-LEVEL"){
			Option_ALEVEL("#id_intent_subject","");
		}
		if ($("#id_intent_level").val()=="IB (Middle Years Programme)"){
			Option_IB_MYP("#id_intent_subject","");
		}
		if ($("#id_intent_level").val()=="IB (Diploma Programme)"){
			Option_IB_DP("#id_intent_subject","");
		}
		if ($("#id_intent_level").val()=="Zhongkao"){
			Option_Zhongkao("#id_intent_subject","");
		}
		if ($("#id_intent_level").val()=="Gaokao"){
			Option_Gaokao("#id_intent_subject","");
		}
	});

	$("#id_intent_subject").change(function(){
		if ($("#id_intent_subject").val()=="Other"){
			$("#id_intent_subject_other").show();
			if ($("#id_intent_level").val()=="O-LEVEL"){
					Option_OLEVEL_OTHER("#id_intent_subject_other");
				}
				if ($("#id_intent_level").val()=="A-LEVEL"){
					Option_ALEVEL_OTHER("#id_intent_subject_other");
				}
				if ($("#id_intent_level").val()=="IB (Middle Years Programme)"){
					Option_IB_MYP_OTHER("#id_intent_subject_other");
				}
				if ($("#id_intent_level").val()=="IB (Diploma Programme)"){
					Option_IB_DP_OTHER("#id_intent_subject_other");
				}
		}
		else
			$("#id_intent_subject_other").hide();
	});


	$("#id_intent_start_time").change(function(){
		if($("#id_intent_start_time").val()=="Other"){
			$("#block_intent_start_time_other").append('<input class="form-control" id="id_intent_start_time_other" type="date" name="intent_start_time_other"/>');
		}
		else{
			$("#block_intent_start_time_other").empty();
		}
	});
	var num_click = 0;
	$("#id_intent_remark5").click(function(){
		if(num_click==0){
			$("#id_remark_other").append('<textarea class="form-control" id="id_intent_remark6" name="intent_remark6" rows="3" placeholder="Other Remarks"></textarea>');
			num_click=1;
		}
		else{
			$("#id_remark_other").empty();
			num_click=0;
		}
	});
});


