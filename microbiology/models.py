from django.db import models


class CultureResult(models.Model):

    SAMPLE_TYPES = [
        ('Blood', 'Blood'),
        ('Urine', 'Urine'),
        ('Sputum', 'Sputum'),
        ('Pus/Swab', 'Pus/Swab'),
        ('Other', 'Other'),
    ]

    RESULT_CHOICES = [
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
    ]

    SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    sample_id = models.CharField(max_length=50, unique=True)

    patient_id = models.CharField(max_length=50)

    patient_name = models.CharField(max_length=100, blank=True)

    patient_age = models.PositiveIntegerField()

    patient_sex = models.CharField(
        max_length=10,
        choices=SEX_CHOICES
    )

    specimen = models.CharField(
        max_length=50,
        choices=SAMPLE_TYPES
    )

    culture_result = models.CharField(
        max_length=20,
        choices=RESULT_CHOICES
    )

    organism = models.CharField(
        max_length=150,
        blank=True
    )

    collection_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.sample_id} - {self.organism}"


class AntibioticSusceptibility(models.Model):

    ANTIBIOTIC_CHOICES = [
        ('Gentamicin', 'Gentamicin'),
        ('Amikacin', 'Amikacin'),
        ('Levofloxacin', 'Levofloxacin'),
        ('Ofloxacin', 'Ofloxacin'),
        ('Ciprofloxacin', 'Ciprofloxacin'),
        ('Ceftazidime', 'Ceftazidime'),
        ('Cefepime', 'Cefepime'),
        ('Cefotaxime', 'Cefotaxime'),
        ('Imipenem', 'Imipenem'),
        ('Meropenem', 'Meropenem'),
        ('Piperacillin', 'Piperacillin'),
        ('Piperacillin-tazobactam', 'Piperacillin-tazobactam'),
        ('Co-trimoxazole', 'Co-trimoxazole'),
        ('Tetracycline', 'Tetracycline'),
    ]

    SUSCEPTIBILITY_CHOICES = [
        ('S', 'S'),
        ('I', 'I'),
        ('R', 'R'),
    ]

    culture = models.ForeignKey(
        CultureResult,
        on_delete=models.CASCADE,
        related_name='susceptibilities'
    )

    antibiotic = models.CharField(
        max_length=100,
        choices=ANTIBIOTIC_CHOICES
    )

    susceptibility = models.CharField(
        max_length=1,
        choices=SUSCEPTIBILITY_CHOICES
    )

    def __str__(self):
        return f"{self.antibiotic} - {self.susceptibility}"
