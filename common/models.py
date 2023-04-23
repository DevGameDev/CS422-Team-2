from django.db import models

# dependencies needed!


class FlexibleDateField(models.DateTimeField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if isinstance(value, str):
            # Try to parse the input string using multiple formats
            try_formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d']
            for format in try_formats:
                try:
                    value = datetime.strptime(value, format)
                    break
                except ValueError:
                    pass
        return super().get_prep_value(value)


class TimeSeriesSetMetadata(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    application_domains = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    min_length = models.IntegerField()
    likes = models.IntegerField()
    num_time_series = models.IntegerField()
    contributors = models.CharField(max_length=255)
    related_paper_reference = models.CharField(max_length=255)
    related_paper_link = models.URLField()


class TimeSeriesMetadata(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    application_domains = models.CharField(max_length=255)
    units = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    vector_size = models.IntegerField()
    length = models.IntegerField()
    set = models.ForeignKey(TimeSeriesSetMetadata, on_delete=models.CASCADE)


class TimeSeriesData(models.Model):
    datetime = FlexibleDateField()
    magnitude = models.FloatField()
    vectorIndex = models.IntegerField()
    metadata = models.ForeignKey(TimeSeriesMetadata, on_delete=models.CASCADE, db_index=True)


class ForecastingTask(models.Model):
    metadata = models.ForeignKey(TimeSeriesMetadata, on_delete=models.CASCADE)
    start_datetime = FlexibleDateField()
    num_forecasts = models.IntegerField()
