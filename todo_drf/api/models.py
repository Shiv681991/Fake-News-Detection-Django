from django.db import models

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title


class Tweets(models.Model):
  tweet_text = models.CharField(max_length=500)
  iids = models.CharField(max_length=100)

  def __str__(self):
    return self.tweet_text


class Tweets_L1(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  iids = models.CharField(max_length=100)

  def __str__(self):
    return self.tweets

class Tweets_L2(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  iids = models.CharField(max_length=100)

  def __str__(self):
    return self.tweets

class Tweets_L3(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)

  def __str__(self):
    return self.tweets


class fact_amd(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets

class fact_amr(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets

class fact_blr(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets

class fact_chn(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets

class fact_dli(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets

class fact_gwt(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets

class fact_hbd(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets

class fact_idr(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets


class fact_jpr(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets


class fact_kpr(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets


class fact_kta(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets


class fact_lko(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets


class fact_mbi(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets


class fact_pne(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets


class fact_rch(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets


class fact_snr(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets


class fact_vns(models.Model):
  tweets = models.CharField(max_length=500)
  direct_claim = models.CharField(max_length=3)
  direct_claim_probability = models.FloatField()
  indirect_claim = models.CharField(max_length=3)
  indirect_claim_probability = models.FloatField()
  opinion = models.CharField(max_length=3)
  opinion_probability = models.FloatField()
  quote = models.CharField(max_length=3)
  quote_probability = models.FloatField()
  not_claim = models.CharField(max_length=3)
  not_claim_probability = models.FloatField()
  level_2 = models.CharField(max_length=15)
  level_2_probability = models.FloatField()
  level_3_tag = models.CharField(max_length=15)
  iids = models.CharField(max_length=100)
  def __str__(self):
    return self.tweets




class entaildata(models.Model):
  tweet = models.CharField(max_length=500)
  FNF = models.CharField(max_length=10)
  prob = models.FloatField()
  iids = models.CharField(max_length=100)
  u1 = models.CharField(max_length=300)
  u2 = models.CharField(max_length=300)
  u3 = models.CharField(max_length=300)
  u4 = models.CharField(max_length=300)
  u5 = models.CharField(max_length=300)
  u6 = models.CharField(max_length=300)
  u7 = models.CharField(max_length=300)
  u8 = models.CharField(max_length=300)
  u9 = models.CharField(max_length=300)
  u10 = models.CharField(max_length=300)

  def __str__(self):
    return self.tweet


class entail_dli(models.Model):
  tweet = models.CharField(max_length=500)
  FNF = models.CharField(max_length=10)
  prob = models.FloatField()
  iids = models.CharField(max_length=100)
  u1 = models.CharField(max_length=300)
  u2 = models.CharField(max_length=300)
  u3 = models.CharField(max_length=300)
  u4 = models.CharField(max_length=300)
  u5 = models.CharField(max_length=300)
  u6 = models.CharField(max_length=300)
  u7 = models.CharField(max_length=300)
  u8 = models.CharField(max_length=300)
  u9 = models.CharField(max_length=300)
  u10 = models.CharField(max_length=300)

  def __str__(self):
    return self.tweet

