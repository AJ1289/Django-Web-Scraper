$(document).ready(function(){
	$('#b_ds').click(function(){
		var c=$('#ds').val()
    $.ajax({
    url:'/url1/',
    type:'POST',
    data:{'url':c},


    success:function(response){
      if(response=='success'){
        alert('File Saved Successfully')
       }

     },
    error:function(xhr,textStatus,thrownError){
      alert('Please Enter Url')
      }





  });

  });
 // ########################################################################################
 $('#b_dl').click(function(){
		var c=$('#dl').val()
    $.ajax({
    url:'/links/',
    type:'POST',
    data:{'web':c},


    success:function(response){
      if(response=='link_success'){
        alert('File Saved Successfully')
       }

     },
    error:function(xhr,textStatus,thrownError){
      alert('Please Enter Url')
      }
    });
   });
//#############################################################################################
$('#b_dt').click(function(){
		var c=$('#dt').val()
    $.ajax({
    url:'/texts/',
    type:'POST',
    data:{'text':c},


    success:function(response){
      if(response=='text_success'){
        alert('File Saved Successfully')
       }

     },
    error:function(xhr,textStatus,thrownError){
      alert('Please Enter Url')
      }
    });
   });
});