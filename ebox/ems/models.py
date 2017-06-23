# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.


from django.db import models




class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'



class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EbAd(models.Model):
    url = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    image_id = models.IntegerField()
    type = models.IntegerField()
    status = models.IntegerField()
    force_flag = models.IntegerField()
    create_time = models.IntegerField()
    expire_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_ad'


class EbArea(models.Model):
    name = models.CharField(max_length=100)
    pid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_area'


class EbBlacklist(models.Model):
    mobile = models.CharField(max_length=11, blank=True, null=True)
    terminal_id = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_blacklist'


class EbBranch(models.Model):
    user_id = models.IntegerField()
    express_name = models.CharField(max_length=245)
    name = models.CharField(max_length=245)
    addr = models.CharField(max_length=245)
    telphone = models.CharField(max_length=45)
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_branch'


class EbBranchBand(models.Model):
    branch_id = models.IntegerField()
    storer_id = models.IntegerField()
    collect = models.IntegerField()
    status = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_branch_band'


class EbCard(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=10)
    key = models.CharField(max_length=10)
    status = models.IntegerField()
    reg_time = models.IntegerField()
    update_time = models.IntegerField()
    person_number = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_card'


class EbClerk(models.Model):
    user_id = models.IntegerField()
    clerk_mobile = models.CharField(max_length=24)
    last_cvt_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_clerk'


class EbCommunicat(models.Model):
    type = models.IntegerField()
    content = models.CharField(max_length=128)
    appid = models.CharField(max_length=64)
    online = models.IntegerField()
    client_id = models.CharField(max_length=64)
    last_update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_communicat'


class EbContainer(models.Model):
    terminal_id = models.IntegerField()
    type = models.SmallIntegerField()
    group = models.CharField(max_length=1)
    name = models.IntegerField()
    size = models.IntegerField()
    status = models.IntegerField()
    purpose = models.IntegerField()
    disable = models.IntegerField()
    detector = models.IntegerField()
    expired_time = models.IntegerField()
    oauth_token = models.CharField(max_length=32)
    package_count = models.IntegerField()
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_container'


class EbContainerUseing(models.Model):
    container_id = models.IntegerField()
    out_time = models.IntegerField()
    send_package_id = models.IntegerField()
    token = models.CharField(max_length=245)
    status = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_container_useing'


class EbContainerWarning(models.Model):
    community_id = models.IntegerField()
    terminal_id = models.IntegerField()
    container_id = models.IntegerField()
    type = models.IntegerField()
    status = models.IntegerField()
    reg_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_container_warning'


class EbConvenient(models.Model):
    applicant = models.IntegerField()
    applicant_name = models.CharField(max_length=64)
    profit_user = models.IntegerField()
    terminal_id = models.IntegerField()
    margin = models.DecimalField(max_digits=7, decimal_places=2)
    margin_ratio = models.IntegerField()
    margin_pay = models.DecimalField(max_digits=7, decimal_places=2)
    business_start_time = models.SmallIntegerField()
    business_end_time = models.SmallIntegerField()
    mailing_money = models.DecimalField(max_digits=7, decimal_places=2)
    send_money = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'eb_convenient'


class EbCvtClkPriv(models.Model):
    convenient_id = models.IntegerField()
    clerk_id = models.IntegerField()
    clerk_name = models.CharField(max_length=32)
    role_id = models.CharField(max_length=64)
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_cvt_clk_priv'


class EbDiscountPay(models.Model):
    user_id = models.IntegerField()
    package_id = models.IntegerField()
    pay = models.DecimalField(max_digits=12, decimal_places=2)
    reg_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_discount_pay'


class EbEboxer(models.Model):
    mobile = models.CharField(max_length=40)
    name = models.CharField(max_length=11)
    code = models.CharField(max_length=64)
    salt = models.CharField(max_length=32)
    real_name = models.CharField(max_length=20)
    rights = models.CharField(max_length=300)
    status = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    lastlogin_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_eboxer'


class EbExpress(models.Model):
    express_name = models.CharField(max_length=128)
    code = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_express'


class EbFavourableLog(models.Model):
    send_package_id = models.IntegerField()
    user_id = models.IntegerField()
    orig_price = models.DecimalField(max_digits=12, decimal_places=2)
    favourable_price = models.DecimalField(max_digits=12, decimal_places=2)
    mail_discount_id = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_favourable_log'


class EbFeedback(models.Model):
    count = models.CharField(max_length=255)
    imgadress = models.CharField(max_length=121)
    apptype = models.IntegerField()
    packagename = models.CharField(max_length=51)
    applytype = models.IntegerField()
    createtime = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'eb_feedback'


class EbHomeDelivery(models.Model):
    time = models.IntegerField()
    endtime = models.IntegerField()
    status = models.IntegerField()
    note = models.CharField(max_length=127, blank=True, null=True)
    eboxer_id = models.IntegerField()
    user_id = models.IntegerField()
    last_user_id = models.IntegerField()
    mobile = models.CharField(max_length=11, blank=True, null=True)
    package_id = models.IntegerField()
    self_name = models.CharField(max_length=127)
    terminal_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_home_delivery'


class EbHomeMail(models.Model):
    mobile = models.CharField(max_length=13)
    time = models.IntegerField(blank=True, null=True)
    endtime = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    note = models.CharField(max_length=127, blank=True, null=True)
    eboxer_id = models.IntegerField()
    user_id = models.IntegerField()
    last_user_id = models.IntegerField()
    terminal_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_home_mail'


class EbHomepage(models.Model):
    name = models.CharField(max_length=255)
    type = models.IntegerField()
    url = models.CharField(max_length=255)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_homepage'


class EbHomepageBind(models.Model):
    homepage_id = models.IntegerField()
    terminal_id = models.IntegerField()
    type = models.IntegerField()
    status = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_homepage_bind'


class EbImage(models.Model):
    type = models.IntegerField()
    adress = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'eb_image'


class EbLabel(models.Model):
    order_id = models.IntegerField()
    content = models.CharField(max_length=245)
    status = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_label'


class EbMailCompany(models.Model):
    name = models.CharField(max_length=25)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_mail_company'


class EbMailDiscount(models.Model):
    model_id = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    status = models.IntegerField()
    code = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.IntegerField()
    limit_money = models.DecimalField(max_digits=11, decimal_places=2)
    discount = models.DecimalField(max_digits=6, decimal_places=2)
    expired_time = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_mail_discount'


class EbMailDiscountModel(models.Model):
    user_id = models.IntegerField()
    model_id = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_mail_discount_model'


class EbMailDiscountModelHis(models.Model):
    weixin_name = models.CharField(max_length=200)
    model_id = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_mail_discount_model_his'


class EbMailDiscountTemporary(models.Model):
    send_package_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_mail_discount_temporary'


class EbMailModel(models.Model):
    type = models.IntegerField()
    limity_money = models.DecimalField(max_digits=11, decimal_places=2)
    discount = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'eb_mail_model'


class EbMatter(models.Model):
    user_id = models.IntegerField()
    convenient_id = models.IntegerField()
    matter_type = models.IntegerField()
    assoc_package_id = models.TextField()
    success_package_id = models.TextField(blank=True, null=True)
    fail_package_id = models.TextField(blank=True, null=True)
    matter_status = models.IntegerField()
    clerk_id = models.IntegerField()
    create_time = models.IntegerField()
    handle_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_matter'


class EbMemorandum(models.Model):
    terminal_id = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    package_name = models.CharField(max_length=50, blank=True, null=True)
    describe = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField()
    handle_time = models.IntegerField()
    reason = models.CharField(max_length=121, blank=True, null=True)
    eboxer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_memorandum'


class EbMessage(models.Model):
    message_type = models.IntegerField()
    user_id = models.IntegerField()
    terminal_id = models.IntegerField()
    message_title = models.CharField(max_length=128)
    message_summary = models.CharField(max_length=1024)
    hide = models.IntegerField()
    last_detail_id = models.IntegerField()
    last_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_message'


class EbMsgDetail(models.Model):
    user_id = models.IntegerField()
    terminal_id = models.IntegerField()
    message_id = models.IntegerField()
    detail_type = models.IntegerField()
    matter_id = models.IntegerField()
    content = models.TextField(blank=True, null=True)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_msg_detail'


class EbOauth(models.Model):
    uuid = models.CharField(max_length=32)
    uuid_expired_time = models.IntegerField()
    user_id = models.IntegerField()
    app_type = models.IntegerField()
    api_key = models.CharField(max_length=64)
    appid = models.CharField(max_length=16)
    status = models.IntegerField()
    gt_client_id = models.CharField(max_length=128, blank=True, null=True)
    weixin_name = models.CharField(max_length=200, blank=True, null=True)
    zfb_name = models.CharField(max_length=100, blank=True, null=True)
    last_login_type = models.IntegerField()
    last_login_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_oauth'


class EbOnekeyorder(models.Model):
    mobile = models.CharField(max_length=11)
    appid = models.IntegerField()
    terminal_id = models.IntegerField()
    package_id = models.IntegerField()
    handle_id = models.IntegerField()
    count = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_onekeyorder'


class EbOperateLog(models.Model):
    container_id = models.IntegerField()
    eboxcer_id = models.IntegerField()
    type = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_operate_log'


class EbPackage(models.Model):
    cid = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.IntegerField()
    terminal_id = models.IntegerField()
    container_id = models.IntegerField()
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11)
    key = models.CharField(max_length=6)
    order_from = models.CharField(max_length=245, blank=True, null=True)
    ifremit = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField()
    status = models.IntegerField()
    images = models.CharField(max_length=256)
    store_time = models.IntegerField()
    book_store_time = models.IntegerField()
    fetch_time = models.IntegerField(blank=True, null=True)
    to_pay = models.DecimalField(max_digits=5, decimal_places=2)
    is_merge = models.IntegerField()
    package_type = models.IntegerField()
    oauth_token = models.CharField(max_length=64, blank=True, null=True)
    pay_status = models.IntegerField()
    pay_money = models.DecimalField(max_digits=5, decimal_places=2)
    pay_red_envelope = models.DecimalField(max_digits=5, decimal_places=2)
    matter_handle = models.IntegerField()
    fetch_pay_sta = models.IntegerField(blank=True, null=True)
    fetch_fee = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'eb_package'


class EbPackageAreward(models.Model):
    package_id = models.IntegerField()
    areward_type = models.IntegerField()
    areward_fee = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_package_areward'


class EbPackageExpand(models.Model):
    package_id = models.IntegerField()
    self_name = models.CharField(max_length=11, blank=True, null=True)
    handover_time = models.IntegerField()
    entering_time = models.IntegerField()
    onshelf_time = models.IntegerField()
    return_reason = models.CharField(max_length=121, blank=True, null=True)
    stand = models.IntegerField()
    fixed_number = models.CharField(max_length=20, blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    last_user_id = models.IntegerField()
    return_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_package_expand'


class EbPackageExtCainiao(models.Model):
    package_id = models.IntegerField()
    sta_order_id = models.CharField(max_length=64)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_package_ext_cainiao'


class EbPackageMerge(models.Model):
    major_package_id = models.IntegerField()
    sub_package_id = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_package_merge'


class EbPackagePay(models.Model):
    user_id = models.IntegerField()
    order_id = models.IntegerField()
    order_from = models.IntegerField()
    money = models.DecimalField(max_digits=12, decimal_places=2)
    recharge_id = models.IntegerField()
    out_trade_no_logs = models.CharField(max_length=30)
    status = models.IntegerField()
    asset_id = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_package_pay'


class EbPickupInform(models.Model):
    id = models.IntegerField(primary_key=True)
    terminal_id = models.IntegerField(blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    packages = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    clerk_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_pickup_inform'


class EbPostageConf(models.Model):
    from_city = models.IntegerField()
    des_city = models.IntegerField()
    mail_company_id = models.IntegerField()
    speed_type = models.IntegerField()
    type = models.IntegerField()
    first_weight = models.DecimalField(max_digits=5, decimal_places=2)
    first_price = models.DecimalField(max_digits=11, decimal_places=2)
    expand_price = models.DecimalField(max_digits=11, decimal_places=2)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_postage_conf'


class EbPostcode(models.Model):
    name = models.CharField(max_length=245)
    number = models.CharField(max_length=10)
    code = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'eb_postcode'


class EbPrivilege(models.Model):
    privilege_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'eb_privilege'


class EbProfit(models.Model):
    user_id = models.IntegerField()
    convenient_id = models.IntegerField()
    matter_id = models.IntegerField()
    repertory_id = models.IntegerField()
    money = models.DecimalField(max_digits=7, decimal_places=2)
    create_time = models.IntegerField()
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_profit'


class EbPromoteA2(models.Model):
    mobile = models.CharField(max_length=11)
    week_of_year = models.IntegerField()
    promote_count = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_promote_a2'


class EbPromoteMobile(models.Model):
    mobile = models.CharField(max_length=11)
    promote_count = models.SmallIntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_promote_mobile'


class EbProvince(models.Model):
    name = models.CharField(max_length=50)
    area_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_province'


class EbRepertory(models.Model):
    user_id = models.IntegerField()
    clerk_id = models.IntegerField()
    terminal_id = models.IntegerField()
    repo_type = models.IntegerField()
    oper_type = models.IntegerField()
    package_id = models.IntegerField()
    divide_into = models.DecimalField(max_digits=4, decimal_places=2)
    margin_pay = models.DecimalField(max_digits=4, decimal_places=2)
    create_time = models.IntegerField()
    handle_time = models.IntegerField(blank=True, null=True)
    name_title = models.CharField(max_length=51, blank=True, null=True)
    name_code = models.CharField(max_length=51, blank=True, null=True)
    clerk_name = models.CharField(max_length=43, blank=True, null=True)
    clerk_mobile = models.CharField(max_length=16, blank=True, null=True)
    mobile = models.CharField(max_length=14, blank=True, null=True)
    images = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_repertory'


class EbRole(models.Model):
    role_name = models.CharField(max_length=32)
    privilege = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'eb_role'


class EbSendPackage(models.Model):
    branch_id = models.IntegerField()
    terminal_id = models.IntegerField()
    container_id = models.IntegerField()
    user_id = models.IntegerField()
    storer_id = models.IntegerField()
    code = models.CharField(max_length=245)
    name = models.CharField(max_length=245, blank=True, null=True)
    label_id = models.IntegerField()
    weight = models.CharField(max_length=10)
    package_charges = models.DecimalField(max_digits=12, decimal_places=2)
    postage = models.DecimalField(max_digits=12, decimal_places=2)
    images = models.CharField(max_length=256, blank=True, null=True)
    package_name = models.CharField(max_length=200, blank=True, null=True)
    order_from = models.CharField(max_length=45, blank=True, null=True)
    reason = models.CharField(max_length=245, blank=True, null=True)
    mail_company_id = models.IntegerField()
    send_addr_id = models.IntegerField()
    receive_addr_id = models.IntegerField()
    status = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    store_time = models.IntegerField()
    confirm_time = models.IntegerField()
    fetch_time = models.IntegerField()
    complte_time = models.IntegerField()
    reject_time = models.IntegerField()
    reject_fetch_time = models.IntegerField()
    cancel_time = models.IntegerField()
    pay_time = models.IntegerField()
    out_time = models.IntegerField()
    matter_handle = models.IntegerField()
    mail_discount_id = models.IntegerField()
    speed_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_send_package'


class EbSendPackageAddr(models.Model):
    send_package_id = models.IntegerField()
    user_id = models.IntegerField()
    send_mobile = models.CharField(max_length=45, blank=True, null=True)
    send_name = models.CharField(max_length=45, blank=True, null=True)
    send_province = models.CharField(max_length=245, blank=True, null=True)
    send_city = models.CharField(max_length=245, blank=True, null=True)
    send_district = models.CharField(max_length=245, blank=True, null=True)
    send_addr = models.CharField(max_length=245, blank=True, null=True)
    send_number = models.CharField(max_length=45, blank=True, null=True)
    receiver_name = models.CharField(max_length=45, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=45, blank=True, null=True)
    receiver_province = models.CharField(max_length=245, blank=True, null=True)
    receiver_city = models.CharField(max_length=245, blank=True, null=True)
    receiver_district = models.CharField(max_length=245, blank=True, null=True)
    receiver_addr = models.CharField(max_length=245, blank=True, null=True)
    receiver_number = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)
    connect = models.IntegerField(blank=True, null=True)
    connect_time = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_send_package_addr'


class EbShareLog(models.Model):
    package_id = models.IntegerField()
    discount_id = models.IntegerField()
    mobile = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'eb_share_log'


class EbStationOrder(models.Model):
    terminal_id = models.IntegerField()
    transaction_num = models.CharField(max_length=50)
    alipay_num = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField()
    money = models.DecimalField(max_digits=12, decimal_places=2)
    pay_mode = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    end_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_station_order'


class EbStationRelationorder(models.Model):
    station_order_id = models.IntegerField()
    money = models.DecimalField(max_digits=12, decimal_places=2)
    send_package_id = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_station_relationorder'


class EbStorer(models.Model):
    user_id = models.IntegerField()
    images = models.CharField(max_length=200, blank=True, null=True)
    express_images = models.CharField(max_length=200)
    real_name = models.CharField(max_length=200, blank=True, null=True)
    person_number = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField()
    card_id = models.IntegerField()
    cancel = models.IntegerField()
    reg_time = models.IntegerField()
    company_id = models.IntegerField(blank=True, null=True)
    reason_id = models.CharField(max_length=245, blank=True, null=True)
    reason_image = models.CharField(max_length=245, blank=True, null=True)
    reason_express = models.CharField(max_length=245, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_storer'


class EbTenement(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=245)
    status = models.IntegerField()
    reg_time = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_tenement'


class EbTenementIncome(models.Model):
    user_id = models.IntegerField()
    tenement_id = models.IntegerField()
    money = models.DecimalField(max_digits=12, decimal_places=2)
    createtime = models.IntegerField()
    updatetime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_tenement_income'


class EbTenementTerminal(models.Model):
    terminal_id = models.IntegerField()
    tenement_id = models.IntegerField()
    status = models.IntegerField()
    profits = models.DecimalField(max_digits=11, decimal_places=2)
    reg_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_tenement_terminal'


class EbTerminal(models.Model):
    terminal_type = models.IntegerField()
    name = models.CharField(unique=True, max_length=64, blank=True, null=True)
    terminal_name = models.CharField(max_length=50)
    province_id = models.IntegerField()
    city_id = models.IntegerField()
    country_id = models.IntegerField()
    addr = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
    contact = models.CharField(max_length=50)
    business_start_time = models.SmallIntegerField()
    business_end_time = models.SmallIntegerField()
    reg_time = models.IntegerField()
    update_time = models.IntegerField()
    status = models.IntegerField()
    refuse = models.CharField(max_length=255)
    delivery_oauth = models.IntegerField()
    mail_oauth = models.IntegerField()
    branch_id = models.IntegerField()
    bonus_ratio = models.IntegerField()
    version = models.CharField(max_length=64)
    price_s = models.DecimalField(max_digits=7, decimal_places=2)
    price_m = models.DecimalField(max_digits=7, decimal_places=2)
    price_l = models.DecimalField(max_digits=7, decimal_places=2)
    wx_qrcode_imgurl = models.CharField(max_length=200, blank=True, null=True)
    wx_qrcode = models.CharField(max_length=200, blank=True, null=True)
    zfb_qrcode_imgurl = models.CharField(max_length=200, blank=True, null=True)
    zfb_qrcode = models.CharField(max_length=200, blank=True, null=True)
    fetch_pay = models.IntegerField()
    fetch_fee = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'eb_terminal'


class EbTerminalDeliver(models.Model):
    user_id = models.IntegerField()
    terminal_id = models.IntegerField()
    status = models.IntegerField()
    unique_id = models.CharField(max_length=3)
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_terminal_deliver'


class EbTerminalEboxer(models.Model):
    terminal_id = models.IntegerField()
    eboxer_id = models.IntegerField()
    status = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_terminal_eboxer'


class EbTerminalExtCainiao(models.Model):
    terminal_id = models.IntegerField()
    station_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'eb_terminal_ext_cainiao'


class EbTerminalImage(models.Model):
    terminal_id = models.IntegerField()
    image_id = models.IntegerField()
    type = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_terminal_image'


class EbTerminalPrice(models.Model):
    terminal_id = models.IntegerField()
    base_price = models.DecimalField(max_digits=5, decimal_places=2)
    special_package_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    modify_mobile = models.DecimalField(max_digits=5, decimal_places=2)
    re_sms = models.DecimalField(max_digits=5, decimal_places=2)
    re_voice_sms = models.DecimalField(max_digits=5, decimal_places=2)
    twice_price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField()
    create_time = models.IntegerField()
    modify_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_terminal_price'


class EbUser(models.Model):
    user_id = models.IntegerField()
    weixin_name = models.CharField(max_length=200, blank=True, null=True)
    zfb_name = models.CharField(max_length=100, blank=True, null=True)
    store_status = models.IntegerField()
    tenement_status = models.IntegerField()
    real_name = models.CharField(max_length=200, blank=True, null=True)
    person_number = models.CharField(max_length=45, blank=True, null=True)
    images = models.CharField(max_length=245, blank=True, null=True)
    valid_status = models.IntegerField(blank=True, null=True)
    reason = models.CharField(max_length=245, blank=True, null=True)
    clientid = models.CharField(max_length=245, blank=True, null=True)
    apptype = models.IntegerField(blank=True, null=True)
    average_store = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    average_fetch = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    interval_fetch = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    reg_time = models.IntegerField()
    update_time = models.IntegerField()
    mobile = models.CharField(max_length=45, blank=True, null=True)
    discount = models.DecimalField(max_digits=12, decimal_places=2)
    ratio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_user'


class EbUserAddr(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=45)
    telphone = models.CharField(max_length=45)
    province = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    addr = models.CharField(max_length=245)
    number = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)
    addr_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_user_addr'


class EbVersion(models.Model):
    version_name = models.CharField(max_length=20)
    message = models.TextField()
    url = models.CharField(max_length=245)
    version_code = models.IntegerField()
    package_name = models.CharField(max_length=80)
    file_name = models.CharField(max_length=82)
    size = models.IntegerField()
    appgroup = models.IntegerField()
    apptype = models.IntegerField()
    type = models.IntegerField()
    app_code = models.IntegerField()
    force_update = models.IntegerField()
    beginat = models.IntegerField(db_column='beginAt')  # Field name made lowercase.
    create_time = models.IntegerField()
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eb_version'


class EbWarn(models.Model):
    terminal_num = models.CharField(max_length=64)
    cabinet_id = models.SmallIntegerField()
    open_type = models.IntegerField()
    package_id = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_warn'


class EbWeixinToken(models.Model):
    id = models.IntegerField(primary_key=True)
    token = models.CharField(max_length=255)
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_weixin_token'


class EbYunfeeGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_yunfee_group'


class EbYunfeeGroupBand(models.Model):
    group_id = models.IntegerField()
    area_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eb_yunfee_group_band'
