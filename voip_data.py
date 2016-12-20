# handiVOIP.py
# 
# 



# Variables & Definitions
polyuc_url = 'dc.nextiva.com/uc{}/'

# Tables & Data
poly_servers = {
	'ip321':  polyuc_url.format('321'),
	'ip331':  polyuc_url.format('331'),
	'ip335':  poly_url.format('335'),
	'ip450':  poly_url.format('450'),
	'ip550':  poly_url.format('550'),
	'ip560':  poly_url.format('560'),
	'ip650':  poly_url.format('650'),
	'ip670':  poly_url.format('670'),
	'ip5000': poly_url.format('5000'),
	'ip6000': poly_url.format('6000'),
	'ip7000': poly_url.format('7000'),
# VVX Models
	'vvx101': 
	
	}
	
# Functions & Operations
print(poly_servers)
mportant Notes

If the phones are not on the UC configuration files then there are only 2 tags you can use: %SBC_TRANSPORT% and %LOCAL_PORT%.


Anything that enables or disables features should be a 0 or a 1 only.


Registration Settings

This section will have all of the tags that affect the registration of the phone.


SBC_TRANSPORT

This sets the transport type for the phone.

    Default Value: UDPonly
    Possible Values: UDPonly (Default), TCPonly
    Example - Tag Name: SBC_TRANSPORT - Tag Value: TCPonly


LOCAL_PORT

This sets the contact port that the phone uses.

    Default Value: 5062
    Recommended Values: 5070 through 5090
    Example - Tag Name: LOCAL_PORT - Tag Value: 5070


Line Key Settings

This section applies to the line keys on the phone. X refers to the registration that you wish to adjust.


REG_X_LABEL

This will prepend the value in this tag to the line key label which is the extension. So if the customer wants the key to say Office then you could set REG_X_LABEL to "Office-" and then the key would say "Office-1001"

    Default Value: none
    Recommended Values: N/A - Dependent on customer recommendation. Common requests include a name or title.
    Example - Tag Name: REG_1_LABEL - Tag Value: Bob -


REG_X_KEYS

This will set how many line keys the selected registration has.

    Default Value : 1
    Possible Values: Can be set up to the maximum amount of lines possible, dependent on the model of phone.
    Example - Tag Name: REG_1_KEYS - Tag Value: 4


Softkey Settings

This section will have all of the tags to turn on or off softkeys. These all have a valid value of either 0 or 1. Softkeys that use FACs on active calls will not work if the phone has multiple registrations.


REJECT_SHARED

This will display a soft key to reject an incoming call.

    Possible Values: 0= Display a soft key for reject, 1 = Do not display the soft key
    Example - Tag Name: REJECT_SHARED - Tag Value: 0


REDUNDANT_KEYS

This will turn on or off the extra softkeys that have hard keys on the phone. For example, the phones have conference, transfer, and hold buttons on the phone so the softkeys are removed for these. This value doesn't apply to the 3xx series as they do not have these hardkeys.

    Default Value: 0
    Possible Values: 0 (Default), 1
    Example - Tag Name: REDUNDANT_KEYS - Tag Value: 1


CALLERS_KEY

Turns on and off the callers key.

    Default Value: 0
    Possible Values: 0 (Default), 1
    Example - Tag Name: CALLERS_KEY - Tag Value: 1


FORWARD_KEY

This will turn on or off the forwarding key on the phone.

    Default Value: 1
    Possible Values: 1 (Default), 0
    Example - Tag Name: FORWARD_KEY - Tag Value: 0


NEWCALL_KEY

Turns on or off the new call key.

    Default Value: 0
    Possible Values: 0 (Default), 1
    Example - Tag Name: NEWCALL_KEY - Tag Value: 1


PTT_KEY

Turns on or off a Push To Talk key.

    Default Value: 0
    Possible Values: 0 (Default), 1
    Example - Tag Name: PTT_KEY - Tag Value: 1


PULL_KEY

Turns on or off a Pull key to retrieve calls from other endpoints.

    Default Value: 0
    Possible Values: 0 (Default), 1
    Example - Tag Name: PULL_KEY - Tag Value: 1


PARK_KEY

Turns on or off park and unpark buttons.

    Default Value: 0
    Possible Value: 0 (Default),
    Example - Tag Name: - Tag Value: 1


SENDVM_KEY

This key is displayed when a call is active. When pressed, it prompts for a user extension to transfer to Voice Messaging. The call is transferred to this user’s Voice Messaging.

    Default Value: 1
    Possible Values: 1 (Default), 0
    Example - Tag Name: SENDVM_KEY - Tag Value: 1


DPICKUP_KEY

Turns on or off a Directed Pickup key.

    Default Value: 1
    Possible Values: 1 (Default), 0
    Example - Tag Name: DPICKUP_KEY - Tag Value: 1


BXFER_KEY

Turns on or off a BlindX key that will do blind transfers.

    Default Value: 1
    Possible Values: 1 (Default), 0
    Example - Tag Name: BXFER_KEY - Tag Value: 1


MISSED CALL TRACKING & REMOVAL

This tag will remove the missed call message on Polycoms

    Example - Tag Name: CUSTOM-1 - Tag Value: call.missedCallTracking.1.enabled
    Example - Tag Name: VALUE-1 - Tag Value: 0


Backgrounds

Custom backgrounds can be set in the phone with these tags. They can be set to URLs and require the images to be the proper size and be .jpg files. These images must be hosted on a web server somewhere. You can also upload the image in the web interface.


    BACKGROUND_VVX for VVX models of phone.

    BACKGROUND_HR for 550's and up.

    BACKGROUND_HR_EM for sidecars.

    BACKGROUND_SM for 450's.


ACD and Hoteling Settings

These settings apply to ACD and Hoteling.

    The feature synchronized ACD feature is supported on the SoundPoint IP 320/321/330/331/335, 430, 450, 550, 560, 650, 670 desktop phones and VVX 300, 310, 400, 410, 500 and 600 desktop phones.


FEATURE_SYNC_ACD

Turns on or off the ACD capabilities of the phone.

    Default Value: 0
    Possible Values: 0 (Default), 1
    Example - Tag Name: FEATURE_SYNC_ACD - Tag Value: 1


FEATURE_SYNC_ACD_PREMIUM

This turns on the agent unavailability states on the phone.

    Default Value: 0
    Possible Values: 0 (Default), 1
    Example - Tag Name: FEATURE_SYNC_ACD_PREMIUM - Tag Value: 1


ACD_SIGNIN_STATE

Sets the ACD state of the phone when a user signs in.

    Default Value: none
    Possible Values: This is dependent on the Enterprise level list of ACD states.
    Example - Tag Name: ACD_SIGNIN_STATE - Tag Value: Escalation


HOTELING

Turns on or off the hoteling capability of the phone. When on there will be a login screen to login to the phone using hoteling.

    Default Value: 0
    Possible Values: 0 (Default), 1
    Example - Tag Name: HOTELING - Tag Value: 1


ACD_SIGNALING

Used to set the type of ACD signaling used on Polycom devices. This must be set to "0" for the "SignIn" hoteling soft key to appear and "1" for ACD states to work.

    Default Value: 1
    Possible Values: 0 or 1 (Default)
    Example - Tag Name: ACD_SIGNALING - Tag Value: 0


ACD_LINE

Specifies the registration used for ACD and hoteling. Both of these features have to use the same key.

    Default Value: 1
    Possible Values: Depends on the amount of lines the phone has, for instance for a Polycom 550 it's 1, 2, 3, 4
    Example - Tag Name: ACD_LINE - Tag Value: 1


Web Browser Settings

These settings most likely will not be used as the browser only supports some web standards and overall requires custom written web pages. VVX phones have a more advanced web browser and these settings could be asked for.


APP_BUTTON

This will allow the Applications button to open a URL. This currently has no use unless a customer has a website they wrote for the phone.

    Default Value: none
    Possible Values: n/a


IDLE_DISPLAY

This allows the background of the phone to have a web page displayed. This currently has no use unless a customer has a website they wrote for the phone.

    Default Value: none
    Possible Values: N/A


IDLE_DISPLAY_REFRESH

This sets the refresh rate for the idle display browser.

    Default Value: none
    Possible Values: N/A


SIPVicious

Warning! - Set up with care - These Tags should have NO Value associated with them. These two tags together are the SIP-VISCIOUS protection that we have on by default for all PolyUC phones. By implementing these tags you are removing the phone’s SIP-VISCIOUS protection, and as such the protection has to be set up on the network side.


RV_METHOD

    Possible Values: Intentionally blank
    Example - Tag Name: RV_METHOD - Tag Value: Intentionally blank


RV_REQUEST

    Possible Values: Intentionally blank
    Example - Tag Name: RV_REQUEST - Tag Value: Intentionally blank


Important Note: - These Tags should have NO Value associated with them. These tags will not work on any non-PolyUC phone and should only be used to correct the half-ring/partial ring on Polycom phones on inbound calls that go to VM.


Other Features

WEBUI

This enables the web GUI for Polycom phones. By default any Polycom UC device type will have the web GUI disabled and in order to access it locally you will have to enable this tag.

    Default Value: 0
    Possible Values: 0 (Default), 1
    Example - Tag Name: WEBUI - Tag Value: 1


THEME

Will change the background layout and theme of the phone. This only works on the VVX500 and the VVX600.

    Default Value: Modern
    Possible Values: Classic = Phone will use the classic theme
    Example: Tag Name: Theme - Tag Value: Modern


WEB_LOCKOUT

Locks someone out if they guess the wrong pw a defined number of times.

    Default Value: 1
    Possible Values: 1 = On, 0 = Off
    Example: Tag Name: WEB_LOCKOUT - Tag Value: 0


LOCKOUT_DURATION

Sets the number of seconds they are locked out.

    Default Value: 60
    Possible Values: 60-300
    Example: Tag Name: LOCKOUT_DURATION - Tag Value: 90


LOCKOUT_ATTEMPTS

Sets the number of attempts before they are locked out

    Default Value: 5
    Possible Values: 3-20
    Example: Tag Name: LOCKOUT_ATTEMPTS - Tag Value: 5


DND

This enables or disables Do Not Disturb (DND).

    Default Value: 1
    Possible Values: 0, 1 (Default)
    Example - Tag Name: DND - Tag Value: 0


LOCALHOLDREMINDER

This enables or disables ring back when a call is on hold for a set period of time. To enable, set to 1 and disable by setting to 0.

    Default Value: none
    Possible Values: 0 (Default), 1
    Example - Tag Name: LOCALHOLDREMINDER - Tag Value: 1


LOCALHOLDPERIOD

This value is the period of the ring back. For example, if set to 30 then every 30 seconds the phone would beep letting you know that you have a call on hold.

    Default Value: none
    Possible Values: 1 through 86600
    Example - Tag Name: LOCALHOLDPERIOD - Tag Value: 30


LOCALHOLDDELAY

This is the start delay before the phone starts to beep. For example, if it is set to 90 then after 90 seconds the phone will beep every number of seconds set in %LOCALHOLDPERIOD%.

    Default Value: none
    Possible Values: 1 through 86600
    Example - Tag Name: LOCALHOLDDELAY - Tag Value: 1


PERSISTENT_VOLUME

Enables or disables persistent volume for headset, handset, and speakerphone.

    Default Value: 1
    Possible Values: 1 (Default), 0
    Example - Tag Name: PERSISTENT_VOLUME - Tag Value: 1


ECHO_CANCELLATION

To enable, set the value of the tag to 1. Echo cancellation is used for minor acoustic echo cancellation and will not fix echoes that are caused by playback from a headset or speakerphone being so loud that it bleeds into the microphone.

    Default Value: 0
    Possible Values: 0 (Default), 1
    Example - Tag Name: ECHO_CANCELLATION - Tag Value: 1


BLF_RING

When someone who is monitored on BLF receives a call the phone will ring and show on the display. To disable this feature set to 0.

    Default Value: 1
    Possible Values: 1 (Default), 0
    Example - Tag Name: BLF_RING - Tag Value: 1


CONFERENCE_ADDRESS

Set this to the Conference address set at the enterprise level to get N-Way calling to work.

    Default Value: none
    Possible Values: confnextiva@prod.voipdnsservers.com
    Example - Tag Name: CONFERENCE_ADDRESS - Tag Value: confnextiva@prod.voipdnsservers.com


CALL_WAITING_TONE

This value determines what happens when the phone has a call waiting. The default value is beep which causes the phone to beep in the handset/headset. The ring option causes the phone to ring as if it was not on a call. Lastly there is silent which causes not audible notification. Valid values are beep, ring, and silent.

    Default Value: beep
    Possible Values: beep (Default), ring, silent
    Example - Tag Name: CALL_WAITING_TONE - Tag Value: ring


EHS

The headset mode for the phone's analog headset jack.

    Default Value: 0 (None)
    Possible Values:

        0 (None)
        1 (Jabra)
        2 (Plantronics)
        3 (Sennheiser)

    Example - Tag Name: EHS - Tag Value: 3


HEADSET_MODE

Setting this to 1 turns on headset memory mode.

    Default Value: 0
    Possible Values: 0 (Default), 1
    Example - Tag Name: HEADSET_MODE - Tag Value: 1


DST_ENABLE

Setting this to 0 turns off DST.

    Default Value: 1
    Possible Values: 1 (Default), 0
    Example - Tag Name: - Tag Value: 0


MISSED_CALLS

Turns on or off the missed calls feature.

    Default Value: 1
    Possible Values: 1 (On), 0 (Off)
    Example - Tag Name: MISSED_CALLS - Tag Value: 0


POWER_SAVE

Turns on or off the LCD power saving feature.

    Default Value: 1
    Possible Values: 1 (On), 0 (Off)
    Example - Tag Name: POWER_SAVE - Tag Value: 0


SIDETONE

Adjusts the headset sidetone level from the default in 1 decibel (dB) increments.

    Default Value: 0
    Possible Values: -12 to 12
    Example - Tag Name: SIDETONE - Tag Value: 6


CR_CONTROL (VVX Phones Only)

Enables or disables BroadSoft BroadWorks v20 call recording feature for individual phone lines. This per-line parameter overrides values you set for the parameter.

    Default Value: 0
    Possible Values: 0 (Off), 1 (On)
    Example - Tag Name: CR_CONTROL - Tag Value: 1


CUSTOM_BLF (VVX Phones Only)

This allows you to place the BLF of a user onto a Shared Call Appearance device.

    Default Value: Blank
    Possible Values: example_BLF@nextiva.com
    Example - Tag Name: CUSTOM_BLF - Tag Value: example_BLF@prod.voipdnsservers.com (matching user BLF)


Important Note: After setting Custom Tags you have to rebuild the files. 

