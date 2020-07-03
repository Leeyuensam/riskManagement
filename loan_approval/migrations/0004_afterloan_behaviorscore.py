# Generated by Django 3.0.6 on 2020-07-02 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_approval', '0003_creditlevel_creditlevelpredict'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfterLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ListingKey', models.CharField(max_length=100, unique=True, verbose_name='ListingKey')),
                ('CreditGrade', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='CreditGrade')),
                ('Term', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Term')),
                ('EmploymentStatus', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='EmploymentStatus')),
                ('BorrowerAPR', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='BorrowerAPR')),
                ('BorrowerRate', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='BorrowerRate')),
                ('LenderYield', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='LenderYield')),
                ('ProsperRating_numeric', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='ProsperRating_numeric')),
                ('ProsperScore', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='ProsperScore')),
                ('ListingCategory_numeric', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='ListingCategory_numeric')),
                ('EmploymentStatusDuration', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='EmploymentStatusDuration')),
                ('CurrentCreditLines', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='CurrentCreditLines')),
                ('OpenCreditLines', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='OpenCreditLines')),
                ('TotalCreditLinespast7years', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='TotalCreditLinespast7years')),
                ('CreditScoreRangeLower', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='CreditScoreRangeLower')),
                ('OpenRevolvingAccounts', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='OpenRevolvingAccounts')),
                ('OpenRevolvingMonthlyPayment', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='OpenRevolvingMonthlyPayment')),
                ('InquiriesLast6Months', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='InquiriesLast6Months')),
                ('TotalInquiries', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='TotalInquiries')),
                ('CurrentDelinquencies', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='CurrentDelinquencies')),
                ('DelinquenciesLast7Years', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='DelinquenciesLast7Years')),
                ('PublicRecordsLast10Years', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='PublicRecordsLast10Years')),
                ('PublicRecordsLast12Months', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='PublicRecordsLast12Months')),
                ('BankcardUtilization', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='BankcardUtilization')),
                ('TradesNeverDelinquent_percentage', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='TradesNeverDelinquent_percentage')),
                ('TradesOpenedLast6Months', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='TradesOpenedLast6Months')),
                ('DebtToIncomeRatio', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='DebtToIncomeRatio')),
                ('LoanFirstDefaultedCycleNumber', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='LoanFirstDefaultedCycleNumber')),
                ('LoanMonthsSinceOrigination', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='LoanMonthsSinceOrigination')),
                ('PercentFunded', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='PercentFunded')),
                ('Recommendations', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Recommendations')),
                ('InvestmentFromFriendsCount', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='InvestmentFromFriendsCount')),
                ('Investors', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Investors')),
                ('CreditGrade_encoded', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='CreditGrade_encoded')),
                ('Term_encoded', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Term_encoded')),
                ('BorrowerState_encoded', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='BorrowerState_encoded')),
                ('Occupation_encoded', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Occupation_encoded')),
                ('EmploymentStatus_encoded', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='EmploymentStatus_encoded')),
                ('IsBorrowerHomeowner_encoded', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='IsBorrowerHomeowner_encoded')),
                ('CurrentlyInGroup_encoded', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='CurrentlyInGroup_encoded')),
                ('IncomeVerifiable_encoded', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='IncomeVerifiable_encoded')),
            ],
            options={
                'verbose_name': '贷款用户催收评分',
                'verbose_name_plural': '贷款用户催收评分',
            },
        ),
        migrations.CreateModel(
            name='BehaviorScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CUST_ID', models.CharField(max_length=100, unique=True, verbose_name='用户ID')),
                ('Loan_Amount', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='贷款额')),
                ('OS', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='逾期贷款')),
                ('Payment', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='支付贷款')),
                ('Spend', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='消费')),
                ('delq', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='逾期情况')),
                ('maxDelqL3M_Bin_WOE', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='maxDelqL3M_Bin_WOE')),
                ('increaseUrateL6M_Bin_WOE', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='increaseUrateL6M_Bin_WOE')),
                ('M2FreqL3M_Bin_WOE', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='M2FreqL3M_Bin_WOE')),
                ('avgUrateL1M_Bin_WOE', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='avgUrateL1M_Bin_WOE')),
                ('M0FreqL3M_WOE', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='M0FreqL3M_WOE')),
                ('avgUrateL3M_Bin_WOE', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='avgUrateL3M_Bin_WOE')),
                ('M1FreqL6M_Bin_WOE', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='M1FreqL6M_Bin_WOE')),
                ('maxDelqL1M_Bin_WOE', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='maxDelqL1M_Bin_WOE')),
                ('avgPayL6M_Bin_WOE', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='avgPayL6M_Bin_WOE')),
                ('M1FreqL12M_Bin_WOE', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='M1FreqL12M_Bin_WOE')),
                ('intercept', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='intercept')),
            ],
            options={
                'verbose_name': '贷款用户行为评分',
                'verbose_name_plural': '贷款用户行为评分',
            },
        ),
    ]
