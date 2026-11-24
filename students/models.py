from django.db import models


class Student(models.Model):
    class Status(models.TextChoices):
        ENROLLED = "Enrolled"
        PENDING = "Pending"
        DROPPED = "Dropped"

    # Personal info
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60)
    sex = models.CharField(max_length=10)
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=120, blank=True)
    nationality = models.CharField(max_length=60, default="Filipino")
    religion = models.CharField(max_length=60, blank=True)
    civil_status = models.CharField(max_length=20, default="Single")

    # Background info
    father_name = models.CharField(max_length=120, blank=True)
    father_occupation = models.CharField(max_length=80, blank=True)
    mother_name = models.CharField(max_length=120, blank=True)
    mother_occupation = models.CharField(max_length=80, blank=True)
    guardian_name = models.CharField(max_length=120, blank=True)
    guardian_relationship = models.CharField(max_length=40, blank=True)
    guardian_contact = models.CharField(max_length=30, blank=True)
    previous_school = models.CharField(max_length=160, blank=True)

    # Academic info
    course = models.CharField(max_length=120)
    year_level = models.PositiveSmallIntegerField()
    section = models.CharField(max_length=20)
    school_year = models.CharField(max_length=9, default="2026-2027")
    semester = models.CharField(max_length=10, default="1st")
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDING)

    # Contact & address
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=80, blank=True)
    province = models.CharField(max_length=80, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    @property
    def full_name(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}".strip()

    @property
    def initials(self):
        return (self.first_name[:1] + self.last_name[:1]).upper()

    def __str__(self):
        return f"{self.student_id} - {self.full_name}"