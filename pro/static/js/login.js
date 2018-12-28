$(document).ready(function(){
  $('#Submit').click(function(){
  
  var use=$('#User_name').val();
  var pas=$('#Pass_word').val();
  if(use==' '){
    alert("null values")
  }
  else{
  $.ajax({
    url:'/log/',
    type:'POST',
    data:{'uname':use,'pword':pas },
 
    success:function(response){
    	if(response=='log_success'){
    		window.location.href='home/'
        var use=''
        var pas=''
    	
    	}
      },


   	error:function(xhr,textStatus,thrownError){
      alert('Log_Error')
      }
    

   });
  }
 });  
});	