from django.db import models

# Create your models here.

class AppTranslations(models.Model):
    idioma_id_idioma = models.OneToOneField('Idioma', models.DO_NOTHING, db_column='idioma_id_idioma', primary_key=True)
    plant_species = models.CharField(max_length=100, blank=True, null=True)
    plant_name = models.CharField(max_length=100, blank=True, null=True)
    plant_family = models.CharField(max_length=100, blank=True, null=True)
    plant_height = models.CharField(max_length=100, blank=True, null=True)
    plant_habitat = models.CharField(max_length=100, blank=True, null=True)
    plant_distribution = models.CharField(max_length=100, blank=True, null=True)
    plant_common_name = models.CharField(max_length=100, blank=True, null=True)
    plant_synonomy = models.CharField(max_length=100, blank=True, null=True)
    plant_curiosity = models.CharField(max_length=100, blank=True, null=True)
    plant = models.CharField(max_length=100, blank=True, null=True)
    leaf = models.CharField(max_length=100, blank=True, null=True)
    flower = models.CharField(max_length=100, blank=True, null=True)
    fruit = models.CharField(max_length=100, blank=True, null=True)
    gastronomy_uses = models.CharField(max_length=100, blank=True, null=True)
    medicinal_uses = models.CharField(max_length=100, blank=True, null=True)
    others_uses = models.CharField(max_length=100, blank=True, null=True)
    map = models.CharField(max_length=100, blank=True, null=True)
    technical_information = models.CharField(max_length=50, blank=True, null=True)
    author_name = models.CharField(max_length=100, blank=True, null=True)
    more_information_about_author = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    tipo_obra = models.CharField(max_length=50, blank=True, null=True)
    artifact_name = models.CharField(max_length=50, blank=True, null=True)
    biography = models.CharField(max_length=100, blank=True, null=True)
    obra = models.CharField(max_length=50, blank=True, null=True)
    plant_flowering_season = models.CharField(max_length=100, blank=True, null=True)
    plant_used_part = models.CharField(max_length=100, blank=True, null=True)
    plant_perenidade = models.CharField(max_length=100, blank=True, null=True)
    start_trail = models.CharField(max_length=50, blank=True, null=True)
    start_quiz = models.CharField(max_length=50, blank=True, null=True)
    show = models.CharField(max_length=50, blank=True, null=True)
    txt_title_quiz = models.CharField(max_length=100, blank=True, null=True)
    txt_subtitle_quiz = models.CharField(max_length=100, blank=True, null=True)
    txt_points = models.CharField(max_length=50, blank=True, null=True)
    txt_points_interest_list = models.CharField(max_length=1000, blank=True, null=True)
    txt_check = models.CharField(max_length=50, blank=True, null=True)
    txt_correct = models.CharField(max_length=50, blank=True, null=True)
    txt_continue = models.CharField(max_length=50, blank=True, null=True)
    txt_incorrect = models.CharField(max_length=50, blank=True, null=True)
    txt_no_questions_available = models.CharField(max_length=100, blank=True, null=True)
    txt_no_information = models.CharField(max_length=200, blank=True, null=True)
    questions_list = models.CharField(max_length=100, blank=True, null=True)
    number_questions = models.CharField(max_length=50, blank=True, null=True)
    number_questions_answered = models.CharField(max_length=50, blank=True, null=True)
    total_points = models.CharField(max_length=50, blank=True, null=True)
    total_points_user = models.CharField(max_length=50, blank=True, null=True)
    no_server = models.CharField(max_length=100, blank=True, null=True)
    no_internet = models.CharField(max_length=100, blank=True, null=True)
    submit = models.CharField(max_length=20, blank=True, null=True)
    txt_enter = models.CharField(max_length=50, blank=True, null=True)
    txt_forgot_password = models.CharField(max_length=50, blank=True, null=True)
    txt_register = models.CharField(max_length=50, blank=True, null=True)
    search = models.CharField(max_length=20, blank=True, null=True)
    user_location = models.CharField(max_length=50, blank=True, null=True)
    maximum_file_size = models.CharField(max_length=250, blank=True, null=True)
    txt_user_name = models.CharField(max_length=100, blank=True, null=True)
    txt_placeholdeer_user_name = models.CharField(max_length=100, blank=True, null=True)
    txt_fill_in_field = models.CharField(max_length=100, blank=True, null=True)
    txt_user_profile = models.CharField(max_length=100, blank=True, null=True)
    txt_view = models.CharField(max_length=100, blank=True, null=True)
    txt_view_edit = models.CharField(max_length=100, blank=True, null=True)
    txt_view_edit_create = models.CharField(max_length=100, blank=True, null=True)
    txt_view_edit_create_trails = models.CharField(max_length=100, blank=True, null=True)
    txt_view_edit_create_users = models.CharField(max_length=100, blank=True, null=True)
    txt_email = models.CharField(max_length=100, blank=True, null=True)
    txt_email_placeholder = models.CharField(max_length=100, blank=True, null=True)
    txt_confirm_email = models.CharField(max_length=100, blank=True, null=True)
    txt_password = models.CharField(max_length=100, blank=True, null=True)
    txt_password_placeholder = models.CharField(max_length=100, blank=True, null=True)
    txt_confirm_password = models.CharField(max_length=100, blank=True, null=True)
    txt_register_user = models.CharField(max_length=100, blank=True, null=True)
    txt_return = models.CharField(max_length=100, blank=True, null=True)
    txt_different_emails = models.CharField(max_length=100, blank=True, null=True)
    txt_different_passwords = models.CharField(max_length=100, blank=True, null=True)
    host_unreachable = models.CharField(max_length=1000, blank=True, null=True)
    txt_user_mismatch = models.CharField(max_length=1000, blank=True, null=True)
    txt_french = models.CharField(max_length=50, blank=True, null=True)
    txt_english = models.CharField(max_length=30, blank=True, null=True)
    txt_portuguese = models.CharField(max_length=25, blank=True, null=True)
    txt_spanish = models.CharField(max_length=25, blank=True, null=True)
    txt_language = models.CharField(max_length=25, blank=True, null=True)
    txt_correct_answer = models.CharField(max_length=100, blank=True, null=True)
    txt_pergunta = models.CharField(max_length=50, blank=True, null=True)
    txt_answer = models.CharField(max_length=20, blank=True, null=True)
    txt_qr_code = models.CharField(max_length=50, blank=True, null=True)
    poetry = models.CharField(max_length=50, blank=True, null=True)
    painting = models.CharField(max_length=50, blank=True, null=True)
    sculture = models.CharField(max_length=50, blank=True, null=True)
    photo = models.CharField(max_length=50, blank=True, null=True)
    artcraft = models.CharField(max_length=50, blank=True, null=True)
    others = models.CharField(max_length=50, blank=True, null=True)
    upload_video = models.CharField(max_length=50, blank=True, null=True)
    artifact_description = models.CharField(max_length=50, blank=True, null=True)
    photo_artifact = models.CharField(max_length=50, blank=True, null=True)
    photo_about_author_work = models.CharField(max_length=100, blank=True, null=True)
    observations = models.CharField(max_length=50, blank=True, null=True)
    video_trigger = models.CharField(max_length=100, blank=True, null=True)
    author_name1 = models.CharField(max_length=50, blank=True, null=True)
    author_name_placeholder = models.CharField(max_length=100, blank=True, null=True)
    photo_author = models.CharField(max_length=50, blank=True, null=True)
    work_done = models.CharField(max_length=50, blank=True, null=True)
    upload_videos_images_biography = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    subtitle = models.CharField(max_length=50, blank=True, null=True)
    specie_placeholder = models.CharField(max_length=100, blank=True, null=True)
    family_placeholder = models.CharField(max_length=100, blank=True, null=True)
    synomy = models.CharField(max_length=50, blank=True, null=True)
    synonomy_placeholder = models.CharField(max_length=100, blank=True, null=True)
    qr_code_description = models.CharField(max_length=50, blank=True, null=True)
    common_name = models.CharField(max_length=50, blank=True, null=True)
    plant_description = models.CharField(max_length=100, blank=True, null=True)
    leaf_description = models.CharField(max_length=50, blank=True, null=True)
    flower_description = models.CharField(max_length=50, blank=True, null=True)
    fruit_description = models.CharField(max_length=50, blank=True, null=True)
    upload_videos_images_plant = models.CharField(max_length=100, blank=True, null=True)
    upload_videos_images_leaf = models.CharField(max_length=100, blank=True, null=True)
    upload_videos_images_flower = models.CharField(max_length=100, blank=True, null=True)
    upload_videos_images_fruit = models.CharField(max_length=100, blank=True, null=True)
    type_plant = models.CharField(max_length=50, blank=True, null=True)
    trees = models.CharField(max_length=50, blank=True, null=True)
    arbustos = models.CharField(max_length=50, blank=True, null=True)
    herbaceas = models.CharField(max_length=50, blank=True, null=True)
    trepadeiras = models.CharField(max_length=100, blank=True, null=True)
    gastronomy_description = models.CharField(max_length=100, blank=True, null=True)
    upload_videos_images_gastronomy = models.CharField(max_length=100, blank=True, null=True)
    medicine_use = models.CharField(max_length=100, blank=True, null=True)
    upload_videos_images_medicine = models.CharField(max_length=100, blank=True, null=True)
    other_uses = models.CharField(max_length=100, blank=True, null=True)
    upload_videos_images_other_uses = models.CharField(max_length=100, blank=True, null=True)
    delete = models.CharField(max_length=50, blank=True, null=True)
    menu_plants = models.CharField(max_length=50, blank=True, null=True)
    menu_plants_questions = models.CharField(max_length=50, blank=True, null=True)
    menu_authors = models.CharField(max_length=50, blank=True, null=True)
    menu_artifacts = models.CharField(max_length=50, blank=True, null=True)
    menu_artifacts_questions = models.CharField(max_length=50, blank=True, null=True)
    menu_trail_fmvg = models.CharField(max_length=50, blank=True, null=True)
    menu_user = models.CharField(max_length=50, blank=True, null=True)
    menu_change_user = models.CharField(max_length=50, blank=True, null=True)
    menu_quit = models.CharField(max_length=50, blank=True, null=True)
    menu_points_interest = models.CharField(max_length=50, blank=True, null=True)
    menu_points_interest_facts = models.CharField(max_length=50, blank=True, null=True)
    menu_points_interest_facts_questions = models.CharField(max_length=50, blank=True, null=True)
    menu_trails = models.CharField(max_length=50, blank=True, null=True)
    upload_videos_images = models.CharField(max_length=100, blank=True, null=True)
    processing = models.CharField(max_length=100, blank=True, null=True)
    done_submission = models.CharField(max_length=50, blank=True, null=True)
    cancel_submission = models.CharField(max_length=50, blank=True, null=True)
    deleted_succeeded = models.CharField(max_length=100, blank=True, null=True)
    deleted_failed = models.CharField(max_length=255, blank=True, null=True)
    txt_fmvg = models.CharField(max_length=255, blank=True, null=True)
    txt_lost = models.CharField(max_length=255, blank=True, null=True)
    txt_invalid_email = models.CharField(max_length=50, blank=True, null=True)
    txt_email_recover_password = models.CharField(max_length=500, blank=True, null=True)
    txt_recover_password_here = models.CharField(max_length=50, blank=True, null=True)
    txt_account_not_found = models.CharField(max_length=300, blank=True, null=True)
    txt_cancel = models.CharField(max_length=50, blank=True, null=True)
    txt_sendemail = models.CharField(max_length=255, blank=True, null=True)
    txt_recover_pass = models.CharField(max_length=200, blank=True, null=True)
    email_already_used = models.CharField(max_length=100, blank=True, null=True)
    txt_recover_title = models.CharField(max_length=1000, blank=True, null=True)
    txt_password_change_sucess = models.CharField(max_length=255, blank=True, null=True)
    file_config_missing = models.CharField(max_length=1000, blank=True, null=True)
    txt_culture = models.CharField(max_length=50, blank=True, null=True)
    point_of_interest = models.CharField(max_length=50, blank=True, null=True)
    txt_fact = models.CharField(max_length=50, blank=True, null=True)
    txt_search = models.CharField(max_length=50, blank=True, null=True)
    txt_downloading = models.CharField(max_length=50, blank=True, null=True)
    txt_media = models.CharField(max_length=50, blank=True, null=True)
    txt_server_error = models.CharField(max_length=50, blank=True, null=True)
    txt_no_free_space = models.CharField(max_length=255, blank=True, null=True)
    txt_qrcode_invalid_offline = models.CharField(max_length=50, blank=True, null=True)
    txt_ok = models.CharField(max_length=10, blank=True, null=True)
    txt_retry = models.CharField(max_length=20, blank=True, null=True)
    txt_no_trails = models.CharField(max_length=1000, blank=True, null=True)
    txt_discard = models.CharField(max_length=100, blank=True, null=True)
    txt_yes = models.CharField(max_length=20, blank=True, null=True)
    txt_no = models.CharField(max_length=20, blank=True, null=True)
    txt_trail_name = models.CharField(max_length=256, blank=True, null=True)
    txt_continue_question = models.CharField(max_length=100, blank=True, null=True)
    txt_point_interest = models.CharField(max_length=255, blank=True, null=True)
    txt_blocked = models.CharField(max_length=1000, blank=True, null=True)
    txt_msg_displayed = models.CharField(max_length=1000, blank=True, null=True)
    txt_email_in_use = models.CharField(max_length=255, blank=True, null=True)
    txt_edit = models.CharField(max_length=255, blank=True, null=True)
    txt_sign_in = models.CharField(max_length=255, blank=True, null=True)
    txt_create_new_account = models.CharField(max_length=255, blank=True, null=True)
    txt_create = models.CharField(max_length=50, blank=True, null=True)
    txt_recover_password = models.CharField(max_length=255, blank=True, null=True)
    txt_save = models.CharField(max_length=50, blank=True, null=True)
    txt_ranking = models.CharField(max_length=250, blank=True, null=True)
    txt_recover = models.CharField(max_length=50, blank=True, null=True)
    txt_backoffice = models.CharField(max_length=50, blank=True, null=True)
    txt_new_pass = models.CharField(max_length=50, blank=True, null=True)
    txt_pass_min_len = models.CharField(max_length=50, blank=True, null=True)
    txt_register_to_see_ranking = models.CharField(max_length=255, blank=True, null=True)
    txt_recovery_sent = models.CharField(max_length=1000, blank=True, null=True)
    txt_remind_offline = models.CharField(max_length=1000, blank=True, null=True)
    txt_upload_after_answer = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'app_translations'


class Author(models.Model):
    idauthor = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    photo_filename = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=1000, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    trail_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'author'


class AuthorThecnicalInformation(models.Model):
    language = models.OneToOneField('Idioma', models.DO_NOTHING, db_column='language', primary_key=True)
    author_idauthor = models.ForeignKey(Author, models.DO_NOTHING, db_column='author_idauthor')
    biography = models.CharField(max_length=10000, blank=True, null=True)
    biography_video = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    obra = models.CharField(max_length=10000, blank=True, null=True)
    observations = models.CharField(max_length=10000, blank=True, null=True)
    curiosities = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'author_thecnical_information'
        unique_together = (('language', 'author_idauthor'),)


class Countries(models.Model):
    id_country = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'countries'


class Culture(models.Model):
    idculture = models.AutoField(primary_key=True)
    path = models.CharField(max_length=10000, blank=True, null=True)
    georeference = models.CharField(max_length=10000, blank=True, null=True)
    map_image_filename = models.CharField(max_length=10000, blank=True, null=True)
    author_idauthor = models.ForeignKey(Author, models.DO_NOTHING, db_column='author_idauthor', blank=True, null=True)
    tipo_obras_tipo_obra = models.IntegerField()
    photo_culture = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'culture'
        unique_together = (('idculture', 'tipo_obras_tipo_obra'),)


class CultureTechnicalInformation(models.Model):
    language = models.OneToOneField('Idioma', models.DO_NOTHING, db_column='language', primary_key=True)
    culture_idculture = models.IntegerField()
    description = models.CharField(max_length=10000, blank=True, null=True)
    artificat_name = models.CharField(max_length=10000, blank=True, null=True)
    observations = models.CharField(max_length=10000, blank=True, null=True)
    curiosities = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'culture_technical_information'
        unique_together = (('language', 'culture_idculture'),)


class Dictionary(models.Model):
    id_palavra = models.IntegerField(primary_key=True)
    palavra = models.CharField(max_length=100, blank=True, null=True)
    language = models.ForeignKey('Idioma', models.DO_NOTHING, db_column='language')
    definition = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dictionary'
        unique_together = (('id_palavra', 'language'),)


class Facts(models.Model):
    idfacts = models.AutoField(primary_key=True)
    triggers_idtriggers = models.ForeignKey('Triggers', models.DO_NOTHING, db_column='triggers_idtriggers', blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'facts'


class FactsTechnicalInformation(models.Model):
    language = models.CharField(primary_key=True, max_length=2)
    facts_idfacts = models.ForeignKey(Facts, models.DO_NOTHING, db_column='facts_idfacts')
    title = models.CharField(max_length=10000, blank=True, null=True)
    subtitle = models.CharField(max_length=10000, blank=True, null=True)
    description = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'facts_technical_information'
        unique_together = (('language', 'facts_idfacts'),)


class Idioma(models.Model):
    id_idioma = models.CharField(primary_key=True, max_length=2)
    designation = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'idioma'


class Languages(models.Model):
    idlanguages = models.AutoField(primary_key=True)
    language = models.CharField(max_length=45, blank=True, null=True)
    language_code = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'languages'


class Logs(models.Model):
    idlogs = models.AutoField(primary_key=True)
    time_stamp = models.CharField(max_length=45, blank=True, null=True)
    id_poi = models.CharField(max_length=45, blank=True, null=True)
    device_id = models.CharField(max_length=45, blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'logs'


class Plants(models.Model):
    idplants = models.AutoField(primary_key=True)
    species = models.CharField(max_length=10000, blank=True, null=True)
    family = models.CharField(max_length=10000, blank=True, null=True)
    georeference = models.CharField(max_length=100, blank=True, null=True)
    synonomy = models.CharField(max_length=10000, blank=True, null=True)
    height = models.CharField(max_length=10000, blank=True, null=True)
    map_image_filename = models.CharField(max_length=10000, blank=True, null=True)
    path = models.CharField(max_length=10000, blank=True, null=True)
    observations = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants'


class PlantsHasTypePlants(models.Model):
    plants_idplants = models.OneToOneField(Plants, models.DO_NOTHING, db_column='plants_idplants', primary_key=True)
    type_plants_idtype_plants = models.IntegerField()
    type_plants_language = models.CharField(max_length=2)

    class Meta:
        managed = True
        db_table = 'plants_has_type_plants'
        unique_together = (('plants_idplants', 'type_plants_idtype_plants', 'type_plants_language'),)


class PlantsTechnicalInformation(models.Model):
    language = models.OneToOneField(Idioma, models.DO_NOTHING, db_column='language', primary_key=True)
    plants_idplants = models.ForeignKey(Plants, models.DO_NOTHING, db_column='plants_idplants')
    common_name = models.CharField(max_length=10000, blank=True, null=True)
    habitat = models.CharField(max_length=10000, blank=True, null=True)
    distribution = models.CharField(max_length=10000, blank=True, null=True)
    plant_descritpion = models.CharField(max_length=10000, blank=True, null=True)
    leaf_description = models.CharField(max_length=10000, blank=True, null=True)
    flower_description = models.CharField(max_length=10000, blank=True, null=True)
    fruit_description = models.CharField(max_length=10000, blank=True, null=True)
    flowering_season = models.CharField(max_length=10000, blank=True, null=True)
    used_parts = models.CharField(max_length=10000, blank=True, null=True)
    gastronomy_uses = models.CharField(max_length=10000, blank=True, null=True)
    medicinal_uses = models.CharField(max_length=10000, blank=True, null=True)
    others_uses = models.CharField(max_length=10000, blank=True, null=True)
    type_plants_type_plant = models.ForeignKey('TypePlants', models.DO_NOTHING, db_column='type_plants_type_plant', blank=True, null=True)
    name = models.CharField(max_length=10000, blank=True, null=True)
    type_plants_language = models.CharField(max_length=2, blank=True, null=True)
    curiosity = models.CharField(max_length=10000, blank=True, null=True)
    perenidade = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'plants_technical_information'
        unique_together = (('language', 'plants_idplants'),)


class PointsInterest(models.Model):
    id_point_interest = models.AutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'points_interest'


class PointsInterestTechnicalInformation(models.Model):
    language = models.CharField(primary_key=True, max_length=2)
    points_interest_id_point_interest = models.ForeignKey(PointsInterest, models.DO_NOTHING, db_column='points_interest_id_point_interest')
    title = models.CharField(max_length=10000, blank=True, null=True)
    subtitle = models.CharField(max_length=10000, blank=True, null=True)
    description = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'points_interest_technical_information'
        unique_together = (('language', 'points_interest_id_point_interest'),)


class Questions(models.Model):
    idquestions = models.AutoField(primary_key=True)
    correct_answer = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    triggers_idtriggers = models.ForeignKey('Triggers', models.DO_NOTHING, db_column='triggers_idtriggers', blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'questions'


class QuestionsTechnicalInformation(models.Model):
    language = models.CharField(primary_key=True, max_length=2)
    question = models.CharField(max_length=10000, blank=True, null=True)
    answer1 = models.CharField(max_length=10000, blank=True, null=True)
    answer2 = models.CharField(max_length=10000, blank=True, null=True)
    answer3 = models.CharField(max_length=10000, blank=True, null=True)
    questions_idquestions = models.ForeignKey(Questions, models.DO_NOTHING, db_column='questions_idquestions')
    after_answer = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'questions_technical_information'
        unique_together = (('language', 'questions_idquestions'),)


class Resources(models.Model):
    id_resource = models.AutoField(primary_key=True)
    type_point_interest = models.CharField(max_length=100, blank=True, null=True)
    type_media = models.CharField(max_length=5, blank=True, null=True)
    type_data = models.CharField(max_length=100, blank=True, null=True)
    resource_use = models.CharField(max_length=10000, blank=True, null=True)
    plants_idplants = models.ForeignKey(Plants, models.DO_NOTHING, db_column='plants_idplants', blank=True, null=True)
    culture_idculture = models.IntegerField(blank=True, null=True)
    filename = models.CharField(max_length=1000, blank=True, null=True)
    path = models.CharField(max_length=1000, blank=True, null=True)
    language = models.CharField(max_length=2, blank=True, null=True)
    resource_descritpion = models.CharField(max_length=10000, blank=True, null=True)
    cover = models.BooleanField(blank=True, null=True)
    color = models.CharField(max_length=8, blank=True, null=True)
    processed_status = models.CharField(max_length=1, blank=True, null=True)
    multiple_files = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    author_idauthor = models.ForeignKey(Author, models.DO_NOTHING, db_column='author_idauthor', blank=True, null=True)
    error_downloading = models.BooleanField(blank=True, null=True)
    trails_idtrail = models.IntegerField(blank=True, null=True)
    points_interest_id_points_interest = models.IntegerField(blank=True, null=True)
    facts_idfacts = models.IntegerField(blank=True, null=True)
    number_uploads = models.IntegerField(blank=True, null=True)
    time_stamp = models.CharField(max_length=100, blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'resources'


class TipoObras(models.Model):
    tipo_obra = models.AutoField(primary_key=True)
    designacao_tipo_obra = models.CharField(max_length=10000, blank=True, null=True)
    idioma_id_idioma = models.ForeignKey(Idioma, models.DO_NOTHING, db_column='idioma_id_idioma')

    class Meta:
        managed = True
        db_table = 'tipo_obras'
        unique_together = (('tipo_obra', 'idioma_id_idioma'),)


class Trails(models.Model):
    idtrails = models.AutoField(primary_key=True)
    description = models.CharField(max_length=10000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    subtitle = models.CharField(max_length=1000, blank=True, null=True)
    trail_name = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    zoom = models.CharField(max_length=64, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    map_marker_description = models.CharField(max_length=10000, blank=True, null=True)
    radius = models.CharField(max_length=10, blank=True, null=True)
    map_marker_color = models.CharField(max_length=8, blank=True, null=True)
    application = models.CharField(max_length=20, blank=True, null=True)
    default_language = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'trails'


class TrailsTechnicalInformation(models.Model):
    language = models.CharField(primary_key=True, max_length=2)
    title = models.CharField(max_length=1000, blank=True, null=True)
    subtitle = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=10000, blank=True, null=True)
    trails_idtrails = models.ForeignKey(Trails, models.DO_NOTHING, db_column='trails_idtrails')

    class Meta:
        managed = True
        db_table = 'trails_technical_information'
        unique_together = (('language', 'trails_idtrails'),)


class Triggers(models.Model):
    idtriggers = models.AutoField(primary_key=True)
    trigerfilename = models.CharField(max_length=10000, blank=True, null=True)
    path = models.CharField(max_length=10000, blank=True, null=True)
    designation = models.CharField(max_length=10000, blank=True, null=True)
    type_resources_idtype_resources = models.ForeignKey('TypeResources', models.DO_NOTHING, db_column='type_resources_idtype_resources', blank=True, null=True)
    plants_idplants = models.ForeignKey(Plants, models.DO_NOTHING, db_column='plants_idplants', blank=True, null=True)
    culture_idculture = models.IntegerField(blank=True, null=True)
    obj_ra = models.BooleanField(blank=True, null=True)
    type_resource = models.CharField(max_length=25, blank=True, null=True)
    filename_uploaded_file = models.CharField(max_length=10000, blank=True, null=True)
    trigger_name = models.CharField(max_length=100, blank=True, null=True)
    trail_name = models.CharField(max_length=50, blank=True, null=True)
    georeference = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    radius = models.CharField(max_length=10, blank=True, null=True)
    map_marker_color = models.CharField(max_length=8, blank=True, null=True)
    map_marker_description = models.CharField(max_length=10000, blank=True, null=True)
    trigger_code = models.CharField(max_length=50, blank=True, null=True)
    points_interest_id_point_interest = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'triggers'


class TypeDataHasPlants(models.Model):
    type_data_idtype_data = models.IntegerField(primary_key=True)
    plants_idplants = models.ForeignKey(Plants, models.DO_NOTHING, db_column='plants_idplants')

    class Meta:
        managed = True
        db_table = 'type_data_has_plants'
        unique_together = (('type_data_idtype_data', 'plants_idplants'),)


class TypePlants(models.Model):
    designation = models.CharField(max_length=100, blank=True, null=True)
    type_plant = models.IntegerField(primary_key=True)
    language = models.ForeignKey(Idioma, models.DO_NOTHING, db_column='language')

    class Meta:
        managed = True
        db_table = 'type_plants'
        unique_together = (('type_plant', 'language'),)


class TypeResources(models.Model):
    idtype_resources = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'type_resources'


class UserHasQuestions(models.Model):
    user_iduser = models.OneToOneField('Users', models.DO_NOTHING, db_column='user_iduser', primary_key=True)
    questions_idquestions = models.IntegerField()
    points = models.IntegerField(blank=True, null=True)
    answer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_has_questions'
        unique_together = (('user_iduser', 'questions_idquestions'),)


class Users(models.Model):
    iduser = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    countries_id_country = models.ForeignKey(Countries, models.DO_NOTHING, db_column='countries_id_country', blank=True, null=True)
    total_points = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    application_name = models.CharField(max_length=20, blank=True, null=True)
    profile = models.IntegerField(blank=True, null=True)
    recover_key = models.CharField(max_length=50, blank=True, null=True)
    time_stamp_recover = models.DateField(blank=True, null=True)
    number_resources_cache = models.IntegerField(blank=True, null=True)
    max_file_size_upload = models.IntegerField(blank=True, null=True)
    device_name_before = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'


class UsersHasTriggers(models.Model):
    users_iduser = models.OneToOneField(Users, models.DO_NOTHING, db_column='users_iduser', primary_key=True)
    triggers_idtriggers = models.ForeignKey(Triggers, models.DO_NOTHING, db_column='triggers_idtriggers')
    complete = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users_has_triggers'
        unique_together = (('users_iduser', 'triggers_idtriggers'),)