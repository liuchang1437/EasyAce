var count_prefer = 0;
function add_prefer()
{

	if(count_prefer<9){
		count_prefer++;
		temp =  '<div class="row" style="margin-top:20px">'
		temp += '<h2 style="color: #759049; font-size: 20px;">Preference '+count_prefer+'</h2>';
		temp += '<div class="col-xs-5">';
		temp += '<div class="col-xs-12 form-group">';
		temp += '<select class="form-control" id="id_teach_level'+count_prefer+'" name="teach_level'+count_prefer+'">';
		temp += '<option value="" selected="selected">Select level</option> </select> </div>'
		temp += '<div class="col-xs-12 form-group">';
		temp += '<select class="form-control" id="id_teach_sub'+count_prefer+'" name="teach_sub'+count_prefer+'">';
		temp += '<option value="" selected="selected">Select subject</option> </select> </div>';
		temp += '<div class="col-xs-12 form-group">';
		temp += '<select class="form-control" id="id_teach_sub_other'+count_prefer+'" name="teach_sub_other'+count_prefer+'">';
		temp += '<option value="" selected="selected">Select subject</option> </select> </div>';

		temp += '</div> <div class="col-xs-2"> <div id="id_copy_'+count_prefer+'" class="btn btn-default">Copy-></div> </div> <div class="col-xs-5">';

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

		$("#id_copy_"+count_prefer).click(function(){
			s = this.id;
 			num = s[8];
			doc = document.getElementById("id_ref_level" + num);
			for(j=0;j<doc.length;j++)
				if(doc.options[j].text == $("#id_teach_level"+num).val())
				{
					doc.selectedIndex = j;
					SetRefLevel("#id_ref_level"+num, "#id_ref_sub", "#id_ref_score", num);
				}

			doc = document.getElementById("id_ref_sub" + num);
			for(j=0;j<doc.length;j++)
				if(doc.options[j].text == $("#id_teach_sub"+num).val())
				{
					doc.selectedIndex = j;
					SetOtherSubject("#id_ref_level"+num, "#id_ref_sub_other", num);
					if($("#id_teach_sub"+num).val() == "Other")
						$("#block_ref_sub_other"+num).show();
					else
						$("#block_ref_sub_other"+num).hide();
				}

			doc = document.getElementById("id_ref_sub_other" + num);
			for(j=0;j<doc.length;j++)
				if(doc.options[j].text == $("#id_teach_sub_other"+num).val())
				{
					doc.selectedIndex = j;
				}
		});

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
 			SetTeachLevel("#id_teach_level"+num, "#id_teach_sub", num);

		});

		$("#id_teach_sub"+count_prefer).change(function(){
			s = this.name;
			num = s[9];
			 
			$("#id_teach_sub_other"+num).hide();
			if ($(this).val()=="Other"){
				$("#id_teach_sub_other"+num).show();
				$("#id_teach_sub_other"+num).empty();
				SetOtherSubject("#id_teach_level"+num, "#id_teach_sub_other", num);

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

 			SetRefLevel("#id_ref_level"+num, "#id_ref_sub", "#id_ref_score", num);
		});

		$("#id_ref_sub"+count_prefer).change(function(){
			s = this.name;
			num = s[7];
			$("#block_ref_sub_other"+num).hide();
			if ($(this).val()=="Other"){
				$("#block_ref_sub_other"+num).show();
				$("#id_ref_sub_other"+num).empty();
				SetOtherSubject("#id_ref_level"+num, "#id_ref_sub_other", num);

			}
		});



	}
}

var prefer_level = [];
var prefer_other = [];
var prefer_name = [];
var refer_level = [];
var refer_name = [];
var refer_other = [];
var refer_score = [];
var num_prefer = 0;
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

				count = 0;
				for(i=0;i<obj["prefer_level"].length;i++)
				{
					edit = true;
					num_prefer += 1;
					prefer_level[i] = obj["prefer_level"][i];
					prefer_other[i] = obj["prefer_other"][i];
					prefer_name[i] = obj["prefer_name"][i];
					refer_level[i] = obj["refer_level"][i];
					refer_name[i] = obj["refer_name"][i];
					refer_other[i] = obj["refer_other"][i];
					refer_score[i] = obj["refer_score"][i];			
				}
				
					
			},
			error: function(){
			}

		});

	for(i=0;i<num_prefer;i++)
	{
		now = i + 1;
		add_prefer();
		doc = document.getElementById("id_teach_level" + now);
		for(j=0;j<doc.length;j++)
			if(doc.options[j].text == prefer_level[now-1])
			{
				doc.selectedIndex = j;
				SetTeachLevel("#id_teach_level"+now, "#id_teach_sub", now); 
				break;
			}
		doc = document.getElementById("id_teach_sub" + now);
		other = false;
		if(prefer_other[now-1])
		{
			other = true;
			doc.selectedIndex = doc.length - 1;
		}
		else
			for(j=0;j<doc.length;j++)
				if(doc.options[j].text == prefer_name[now-1])
				{
					doc.selectedIndex = j;
					break;
				}
		if(other)
		{
			$("#id_teach_sub_other"+now).show();
			$("#id_teach_sub_other"+now).empty();
			SetOtherSubject("#id_teach_level"+now, "#id_teach_sub_other", now);

			doc = document.getElementById("id_teach_sub_other"+now);
			for(j=0;j<doc.length;j++)
				if(doc.options[j].text == prefer_name[now-1])
				{
					doc.selectedIndex = j;
					break;
				}
		}

		/////////////reference////////////////

		doc = document.getElementById("id_ref_level" + now);
		for(j=0;j<doc.length;j++)
			if(doc.options[j].text == refer_level[now-1])
			{
				doc.selectedIndex = j;
				SetRefLevel("#id_ref_level"+now, "#id_ref_sub", "#id_ref_score", now);
				break;
			}
		doc = document.getElementById("id_ref_sub" + now);
		other = false;
		if(refer_other[now-1])
		{
			other = true;
			doc.selectedIndex = doc.length - 1;
		}
		else
			for(j=0;j<doc.length;j++)
				if(doc.options[j].text == refer_name[now-1])
				{
					doc.selectedIndex = j;
					break;
				}
		if(other)
		{
			$("#block_ref_sub_other"+now).show();
			$("#id_ref_sub_other"+now).empty();

			SetOtherSubject("#id_ref_level"+now, "#id_ref_sub_other", now);
			doc = document.getElementById("id_ref_sub_other"+now);
			for(j=0;j<doc.length;j++)
				if(doc.options[j].text == refer_name[now-1])
				{
					doc.selectedIndex = j;
					break;
				}
		}

		doc = document.getElementById("id_ref_score" + now);
		for(j=0;j<doc.length;j++)
			if(doc.options[j].text == refer_score[now-1])
			{
				doc.selectedIndex = j;
				break;
			}

		i = now - 1;
	}
}

function SetTeachLevel(id_level, id_sub, now)
{
	if ($(id_level).val()=="PSLE"){
		Option_PSLE(id_sub,now);
	}
	if ($(id_level).val()=="AEIS"){
		Option_AEIS(id_sub,now);
	}
	if ($(id_level).val()=="O-LEVEL"){
		Option_OLEVEL(id_sub,now);
	}
	if ($(id_level).val()=="A-LEVEL"){
		Option_ALEVEL(id_sub,now);
	}
	if ($(id_level).val()=="IB (Middle Years Programme)"){
		Option_IB_MYP(id_sub,now);
	}
	if ($(id_level).val()=="IB (Diploma Programme)"){
		Option_IB_DP(id_sub,now);
	}
	if ($(id_level).val()=="Zhongkao"){
		Option_Zhongkao(id_sub,now);
	}
	if ($(id_level).val()=="Gaokao"){
		Option_Gaokao(id_sub,now);
	}
	if ($(id_level).val()=="SAT"){
		Option_SAT(id_sub,now);
	}
}

function SetRefLevel(id_level, id_sub, id_score, now)
{
	if ($(id_level).val()=="O-LEVEL"){
		Option_OLEVEL(id_sub,now);
		Option_score("O-LEVEL",id_score+now);
	}
	if ($(id_level).val()=="A-LEVEL"){
		Option_ALEVEL(id_sub,now);
		Option_score("A-LEVEL",id_score+now);
	}
	if ($(id_level).val()=="IB (Middle Years Programme)"){
		Option_IB_MYP(id_sub,now);
		Option_score("IB (Middle Years Programme)",id_score+now);
	}
	if ($(id_level).val()=="IB (Diploma Programme)"){
		Option_IB_DP(id_sub,now);
		Option_score("IB (Diploma Programme)",id_score+now);
	}
	if ($(id_level).val()=="Zhongkao"){
		Option_Zhongkao(id_sub,now);
		Option_score("Zhongkao",id_score+now);
	}
	if ($(id_level).val()=="Gaokao"){
		Option_Gaokao(id_sub,now);
		Option_score("Gaokao",id_score+now);
	}
}
function SetOtherSubject(id_level, id_sub_other, now)
{
	if ($(id_level).val()=="O-LEVEL"){
		Option_OLEVEL_OTHER(id_sub_other+now);
	}
	if ($(id_level).val()=="A-LEVEL"){
		Option_ALEVEL_OTHER(id_sub_other+now);
	}
	if ($(id_level).val()=="IB (Middle Years Programme)"){
		Option_IB_MYP_OTHER(id_sub_other+now);
	}
	if ($(id_level).val()=="IB (Diploma Programme)"){
		Option_IB_DP_OTHER(id_sub_other+now);
	}
}

$(document).ready(function(){
	get_subjects();
	if(!edit) add_prefer();

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




