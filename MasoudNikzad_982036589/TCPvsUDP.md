# TCP 
**Transmission Control Protocol**

<div dir="rtl">
یک مدل به اصطلاح جهت گرا (connection-oriented)  است که یعنی زمانی که کانکشن بین کلاینت و سرور برقرار شد هم کلاینت میتونه اطاعات برای سرور بفرسته و هم سرور میتونه دیتا برای کلاینت بفرسته
</div>

> <div dir="rtl"> در واقع دیتا میتونه تو هر دو جهت انتقال پیدا کنه </div>
<div dir="rtl">
 و همچنین در مدل TCP این گارانتی و اطمینان وجود داره که حتما پکت به مقصد ارسال میشه 
</div>

><div dir="rtl"> ( به این صورت که دستگاهی که داره پکت ارسال میکنه دایما در حال ارسال اون پکته مادامی که از سمت کلاینت یک acknolgement  دریافت کنه که این پکت به دست من رسیده )</div> 
<div dir="rtl">
این مدل برای ارسال عکس و یا دانلود فایل و محتوا یا تماس های صوتی که هر دو طرف در حال مکالمه با یکدیگر هستند مناسبه
</div>

# UDP
**User Datagram Protocol**

<div dir="rtl">
یک مدل connectionless است به این معنی که دیتا یا به اصطلاح پکت ها فقط از سمت یک دیستگاه ارسال میشن و برای دستگاه ارسال کننده هیچ اهمیتی نداره که دیتا به دست گیرنده رسیده یانه و همچین این مدل ساده تر و هزینه لود کمتری نسبت به مدل TCP داره این مدل برای پخش تلویزیون انلاین یا بازی های انلاین و یا رادیو انلاین مناسبه
</div>




# comparison


| Feature                | TCP                                                                                                             | UDP                                                                                                |
| ---------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Connection status      | Requires an established connection to transmit data (connection should be closed once transmission is complete) | Connectionless protocol with no requirements for opening, maintaining, or terminating a connection |
| Data sequencing        | Able to sequence                                                                                                | Unable to sequence                                                                                 |
| Guaranteed delivery    | Can guarantee delivery of data to the destination router                                                        | Cannot guarantee delivery of data to the destination                                               |
| Retransmission of data | Retransmission of lost packets is possible                                                                      | No retransmission of lost packets                                                                  |
| Error checking         | Extensive error checking and acknowledgment of data                                                             | Basic error checking mechanism using checksums                                                     |
| Method of transfer     | Data is read as a byte stream; messages are transmitted to segment boundaries                                   | UDP packets with defined boundaries; sent individually and checked for integrity on arrival        |
| Speed                  | Slower than UDP                                                                                                 | Faster than TCP                                                                                    |
| Broadcasting           | Does not support Broadcasting                                                                                   | Does support Broadcasting                                                                          |
| Optimal use            | Used by HTTPS, HTTP, SMTP, POP, FTP, etc                                                                        | Video conferencing, streaming, DNS, VoIP, etc                                                      |
