import pyotp 

from sms_ir import SmsIr


def sendToken(user):
    totp = pyotp.TOTP(pyotp.random_base32(), interval=180)
    
    otp = totp.now()
    
    user.otp = otp
    
    print(f"The OTP is : {otp}")
    
    # TODO : send a SMS to User's verified Phone number

    # sms = SmsIr(api_key="", linenumber="09123456789")

    # sms.send_sms(number=user.phone, message="""
    #             کد تایید شما در سامانه
    #         """, linenumber="09123456789")
    
    return otp
