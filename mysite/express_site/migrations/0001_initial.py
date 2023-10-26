# Generated by Django 4.2.6 on 2023-10-26 02:11

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "男"), ("female", "女")],
                        default="male",
                        max_length=10,
                        verbose_name="性别",
                    ),
                ),
                (
                    "address",
                    models.CharField(default="北京", max_length=100, verbose_name="地址"),
                ),
                (
                    "mobile",
                    models.CharField(
                        blank=True, max_length=11, null=True, verbose_name="手机号"
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        default="120@163.com", max_length=50, verbose_name="邮箱"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "用户信息",
                "verbose_name_plural": "用户信息",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Express",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="快递公司")),
            ],
            options={
                "verbose_name": "快递公司",
                "verbose_name_plural": "快递公司",
            },
        ),
        migrations.CreateModel(
            name="ExpressProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=64, verbose_name="姓名")),
                ("phone", models.CharField(max_length=64, verbose_name="手机号")),
                ("area", models.TextField(blank=True, null=True, verbose_name="地区")),
                ("address", models.TextField(blank=True, null=True, verbose_name="地址")),
                (
                    "is_getmsg",
                    models.BooleanField(default=False, verbose_name="是否接收短信提醒"),
                ),
                (
                    "department",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="所属部门"
                    ),
                ),
                (
                    "floor",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="楼层"
                    ),
                ),
                (
                    "employee_id",
                    models.CharField(
                        blank=True, max_length=64, null=True, verbose_name="员工工号"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ParcelProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pnum",
                    models.CharField(db_index=True, max_length=128, verbose_name="订单号"),
                ),
                (
                    "pname",
                    models.CharField(
                        choices=[
                            ("顺丰", "顺丰"),
                            ("圆通", "圆通"),
                            ("中通", "中通"),
                            ("百世", "百世"),
                            ("EMS", "EMS"),
                            ("DHL", "DHL"),
                            ("UPS", "UPS"),
                            ("TNT", "TNT"),
                            ("申通", "申通"),
                            ("韵达", "韵达"),
                            ("京东", "京东"),
                            ("优速", "优速"),
                            ("德邦", "德邦"),
                            ("联邦", "联邦"),
                            ("天天", "天天"),
                            ("国通", "国通"),
                            ("速尔", "速尔"),
                            ("快捷", "快捷"),
                            ("宅急送", "宅急送"),
                        ],
                        default="顺丰",
                        max_length=32,
                        verbose_name="物流名称",
                    ),
                ),
                (
                    "pcargo_num",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=128,
                        null=True,
                        verbose_name="物流单号",
                    ),
                ),
                (
                    "pinfo",
                    models.CharField(default="文件", max_length=128, verbose_name="物品类型"),
                ),
                ("pweight", models.FloatField(default=0.0, verbose_name="快递重量")),
                ("psupport", models.BooleanField(default=False, verbose_name="是否保价")),
                (
                    "psupport_value",
                    models.CharField(
                        blank=True, max_length=32, null=True, verbose_name="保价金额"
                    ),
                ),
                (
                    "pcost",
                    models.FloatField(
                        blank=True, default=0, null=True, verbose_name="快递费用"
                    ),
                ),
                (
                    "ppayment",
                    models.CharField(
                        choices=[("现结", "现结"), ("月结", "月结")],
                        default="现结",
                        max_length=32,
                        verbose_name="结算方式",
                    ),
                ),
                ("remark", models.TextField(blank=True, null=True, verbose_name="备注")),
                (
                    "ptime",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="寄件时间"
                    ),
                ),
                (
                    "pdeliver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="deliver_name",
                        to="express_site.expressprofile",
                        verbose_name="发件人信息",
                    ),
                ),
                (
                    "preceiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver_name",
                        to="express_site.expressprofile",
                        verbose_name="收件人信息",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Province",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128, verbose_name="地区名称")),
            ],
            options={
                "verbose_name": "地区",
                "verbose_name_plural": "地区",
            },
        ),
        migrations.CreateModel(
            name="Weight",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_weight", models.IntegerField(verbose_name="首重")),
                ("continue_weight", models.IntegerField(verbose_name="续重")),
                (
                    "express_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="express_site.express",
                    ),
                ),
                (
                    "province_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="express_site.province",
                    ),
                ),
            ],
            options={
                "verbose_name": "结算信息",
                "verbose_name_plural": "结算信息",
            },
        ),
        migrations.CreateModel(
            name="UserParcelInfo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "parcel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="express_site.parcelprofile",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReceiveParcelProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rcargo_num",
                    models.CharField(
                        db_index=True, max_length=128, verbose_name="快递单号"
                    ),
                ),
                (
                    "rname",
                    models.CharField(
                        choices=[
                            ("顺丰", "顺丰"),
                            ("圆通", "圆通"),
                            ("中通", "中通"),
                            ("百世", "百世"),
                            ("EMS", "EMS"),
                            ("DHL", "DHL"),
                            ("UPS", "UPS"),
                            ("TNT", "TNT"),
                            ("申通", "申通"),
                            ("韵达", "韵达"),
                            ("京东", "京东"),
                            ("优速", "优速"),
                            ("德邦", "德邦"),
                            ("联邦", "联邦"),
                            ("天天", "天天"),
                            ("国通", "国通"),
                            ("速尔", "速尔"),
                            ("快捷", "快捷"),
                            ("宅急送", "宅急送"),
                        ],
                        default="顺丰",
                        max_length=32,
                        verbose_name="物流名称",
                    ),
                ),
                (
                    "rinfo",
                    models.CharField(default="文件", max_length=128, verbose_name="物品类型"),
                ),
                ("remark", models.TextField(blank=True, null=True, verbose_name="备注")),
                (
                    "rtime",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="收件时间"
                    ),
                ),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="name",
                        to="express_site.expressprofile",
                        verbose_name="收件人信息",
                    ),
                ),
            ],
        ),
    ]
