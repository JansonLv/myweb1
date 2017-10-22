$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;
	var error_email = false;
	var error_check = false;


	$('#user_name').blur(function() {
		$('.error_tip_info').hide();
		check_user_name();
	});

	$('#user_pwd2').blur(function() {
		$('.error_tip_info').hide();
		check_pwd();
	});

	$('#user_pwd1').blur(function() {
		$('.error_tip_info').hide();
		check_cpwd();
	});

	$('#user_email').blur(function() {
		$('.error_tip_info').hide();
		check_email();
	});

	$('#user_allow').click(function() {
		if($(this).is(':checked'))
		{
			error_check = false;
			$(this).siblings('span').hide();
		}
		else
		{
			error_check = true;
			$(this).siblings('span').html('请勾选同意');
			$(this).siblings('span').show();
		}
	});


	function check_user_name(){
		var len = $('#user_name').val().length;
		if(len<5||len>20)
		{
			$('#user_name').next().html('请输入5-20个字符的用户名');
			$('#user_name').next().show();
			error_name = true;
		}
		else
		{
			$.get('/users/checkname/',{'username':$('#user_name').val()}, function (data) {
				if(data['ret']){
					$('#user_name').next().html('用户名已存在');
					$('#user_name').next().show();
					error_name = true;
				}
				else{
                	$('#user_name').next().hide();
                	error_name = false;
				}
            });
		}
	}

	function check_pwd(){
		var len = $('#user_pwd1').val().length;
		if(len<8||len>20)
		{
			$('#user_pwd1').next().html('密码最少8位，最长20位')
			$('#user_pwd1').next().show();
			error_password = true;
		}
		else
		{
			$('#user_pwd1').next().hide();
			error_password = false;
		}		
	}


	function check_cpwd(){
		var pass = $('#user_pwd2').val();
		var cpass = $('#user_pwd2').val();

		if(pass!=cpass)
		{
			$('#user_pwd2').next().html('两次输入的密码不一致')
			$('#user_pwd2').next().show();
			error_check_password = true;
		}
		else
		{
			$('#user_pwd2').next().hide();
			error_check_password = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#user_email').val()))
		{
			$('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#user_email').next().html('你输入的邮箱格式不正确')
			$('#user_email').next().show();
			error_check_password = true;
		}

	}


	$('#reg_form').submit(function() {
		$('.error_tip_info').hide();
		check_user_name();
		check_pwd();
		check_cpwd();
		check_email();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});
})
