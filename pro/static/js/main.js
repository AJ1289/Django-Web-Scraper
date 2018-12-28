$(document).ready(function(){
  $('#signupBtn').click(function(){
    var p=0;
    var user=$('#user').val();
    var fstname=$('#fname').val();
    var lstname=$('#lname').val();
    var mailid=$('#Email').val();
    var pass=$('#Pwd').val();
    var rpass=$('#Rpwd').val();
    

    if(fstname=="")
      { 
        $('#emptyError').css("display","inline").fadeOut(3000);
      }
    if(lstname=="")
      {
        $('emptyError').css("display","inline").fadeOut(3000);
      }
    if(user=="")
      {
        $('#emptyError').css("display","inline").fadeOut(3000);
      }
    if(mailid=="")
      {
        $('#emptyError').css("display","inline").fadeOut(3000);
      }
    if(pass=="")
      {
        $('#emptyError').css("display","inline").fadeOut(3000);
      }
    if(rpass=="")
      { 
        $('#emptyError').css("display","inline").fadeOut(3000);
      }
    

  



  $.ajax({
    url:'/send_data/',
    type:'POST',
    data:{'user':user,'frtName':fstname,'lrtName':lstname,
    'mail':mailid,'password':pass,'Rpassword':rpass},

    success:function(response){
      if(response=='success'){
      
         window.location.href='/'
      }

    },
    error:function(xhr,textStatus,thrownError){
      alert('error')
      }

  });
  });



  //======================================================================for login 
 
 






});






