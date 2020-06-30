# Generated by Django 3.0.6 on 2020-06-28 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anti_Fraud_Yes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=224, verbose_name='样本ID')),
                ('label', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='是否作弊')),
                ('pkgname', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='包名(MD5加密)')),
                ('ver', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='APP版本')),
                ('adunitshowid', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='对外广告位ID（MD5加密）')),
                ('mediashowid', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='对外媒体ID（MD5加密）')),
                ('apptype', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='app所属分类')),
                ('nginxtime', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='请求到达服务时间')),
                ('ip', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='客户端IP地址')),
                ('city', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='城市')),
                ('province', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='省份')),
                ('reqrealip', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='请求的http协议头携带IP')),
                ('adidmd5', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Adroid ID的MD5值')),
                ('imeimd5', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='imei的MD5值')),
                ('idfamd5', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='idfa的MD5值')),
                ('openudidmd5', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='openudid的MD5值')),
                ('macmd5', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='mac的MD5值')),
                ('dvctype', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='设备类型')),
                ('model', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='机型')),
                ('make', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='厂商')),
                ('ntt', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='网络类型')),
                ('carrier', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='运营商')),
                ('os', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='操作系统')),
                ('osv', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='操作系统版本')),
                ('orientation', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='横竖屏')),
                ('lan', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='语言')),
                ('h', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='设备高')),
                ('w', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='设备宽')),
                ('ppi', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='屏幕密度')),
            ],
        ),
    ]