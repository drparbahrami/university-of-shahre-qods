# Subnet Mask
### IP Classes

| Class      | Address Range | Subnet masking | Example IP | Leading bits | Max number of networks | Application                                                           |
| ---------- | ------------- | -------------- | ---------- | ------------ | ---------------------- | --------------------------------------------------------------------- |
| IP Class A | 1 to 126      | 255.0.0.0      | 1.1.1.1    | 8            | 128                    | Used for large number of hosts.                                       |
| IP Class B | 128 to 191    | 255.255.0.0    | 128.1.1.1  | 16           | 16384                  | Used for medium size network.                                         |
| IP Class C | 192 to 223    | 255.255.255.0  | 192.1.11.  | 24           | 2097157                | Used for local area network.                                          |
| IP Class D | 224 to 239    | NA             | NA         | NA           | NA                     | Reserve for multi-tasking.                                            |
| IP Class E | 240 to 254    | NA             | NA         | NA           | NA                     | This class is reserved for research and Development Purposes.<br><br> |



## what is subnet mask?

<div dir="rtl">
سیستم ها براي تشخیص تعلق یا عدم تعلق به يك شبكه از مفهومي به نام Subnet Mask استفاده مي كند. به اين صورت كه تمام بيت هاي Network را 1 و تمام بيت هاي Host را 0 در نظر مي گيرد تا Subnet mask را بسازد. در نظر داشته باشید که هر کلاسی که ما میتونیم ازشون به عنوان یک آدرس استفاده کنیم یک SubnetMask استاندارد داره به عبارت دیگر هر ip دارای یک SubnetMask است و برای کلاس هایی که در بالا گفته شد این SubnetMask ها به صورت استاندارد زیر هستند:
</div>

**Standard Subnet Masks:**

Class A : 255.0.0.0
Class B : 255.255.0.0
Class C:  255.255.255.0

<div dir="rtl">
نکته سابنت مسک به دو شکل قابل نمایش هستد:
</div>

 - subnet mask format
 -  prefix format

<div dir="rtl">
در subnet mask format، آی پی مربوطه را به صورت یک ip به همراه subnet mask آن به صورت جداگانه نمایش می دهیم. یعنی یک عدد که IP را نشان میدهد و عددی دیگر یا IP دیگر subnet mask را به عنوان مثال:
</div>

>IP: 192.168..1.2
Subnet mask: 255.255.255.0

<div dir="rtl">
در prefix format آی پی و subnet mask آن را با هم در یک ip نشان میدهید ، یعنی بعد از ip ، یک / (که جداکننده Ip از عدد مربوط به subnet mask هست) قرار میدهیم و سپس یک عدد نوشته میشود که این عدد تعداد 1 هایی که در subnet mask همان ip داریم می باشد به طور مثال:
</div>
> 192.168.1.2/24
