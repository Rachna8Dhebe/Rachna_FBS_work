Full Django + DRF Application (with Front
                               ‑End)
 This is a complete, testable project scaffold that implements all required endpoints and a minimal front-end
 (HTML/CSS/JS) using Django templates and Fetch API.
 Project Structure
 institute/                 # Django project root
 ├─ manage.py
 ├─ requirements.txt
 ├─ institute/
 │  ├─ _init_.py
 │  ├─ settings.py
 │  ├─ urls.py
 │  └─ wsgi.py
 ├─ api/                    # App providing the REST API
 │  ├─ _init_.py
 │  ├─ admin.py
 │  ├─ apps.py
 │  ├─ migrations/
 │  │  └─ _init_.py
 │  ├─ models.py
 │  ├─ serializers.py
 │  ├─ views.py
 │  └─ urls.py              # optional; using router in project urls
 ├─ templates/
 │  └─ index.html           # Front-end UI (HTML + minimal CSS + JS)
 └─ static/
   ├─ css/
   │  └─ styles.css
   └─ js/
      └─
 app.js
 requirements.txt
 django==5.0.6
 djangorestframework==3.15.2
 (You can use current latest stable versions; these are example pins.)
 1
manage.py
 #!/usr/bin/env python
 import os
 import sys
 if _name_ == "_main_":
 os.environ.setdefault("DJANGO_SETTINGS_MODULE", "institute.settings")
 from django.core.management import execute_from_command_line
 execute_from_command_line(sys.argv)
 institute/settings.py
 from pathlib import Path
 import os
 BASE_DIR = Path(_file_).resolve().parent.parent
 SECRET_KEY = "dev-secret-key-change-in-prod"
 DEBUG = True
 ALLOWED_HOSTS = ["*"]
 INSTALLED_APPS = [
 "django.contrib.admin",
 "django.contrib.auth",
 "django.contrib.contenttypes",
 "django.contrib.sessions",
 "django.contrib.messages",
 "django.contrib.staticfiles",
 "rest_framework",
 "api",
 ]
 MIDDLEWARE = [
 "django.middleware.security.SecurityMiddleware",
 "django.contrib.sessions.middleware.SessionMiddleware",
 "django.middleware.common.CommonMiddleware",
 "django.middleware.csrf.CsrfViewMiddleware",
 "django.contrib.auth.middleware.AuthenticationMiddleware",
 "django.contrib.messages.middleware.MessageMiddleware",
 "django.middleware.clickjacking.XFrameOptionsMiddleware",
 ]
 2
ROOT_URLCONF = "institute.urls"
 TEMPLATES = [
 {
 "BACKEND": "django.template.backends.django.DjangoTemplates",
 "DIRS": [BASE_DIR / "templates"],
 "APP_DIRS": True,
 "OPTIONS": {
 "context_processors": [
 "django.template.context_processors.debug",
 "django.template.context_processors.request",
 "django.contrib.auth.context_processors.auth",
 "django.contrib.messages.context_processors.messages",
 ],
 },
 },
 ]
 WSGI_APPLICATION = "institute.wsgi.application"
 # SQLite for simplicity
 DATABASES = {
 "default": {
 "ENGINE": "django.db.backends.sqlite3",
 "NAME": BASE_DIR / "db.sqlite3",
 }
 }
 # Static files
 STATIC_URL = "/static/"
 STATICFILES_DIRS = [BASE_DIR / "static"]
 # DRF basic config (optional)
 REST_FRAMEWORK = {
 "DEFAULT_RENDERER_CLASSES": [
 "rest_framework.renderers.JSONRenderer",
 "rest_framework.renderers.BrowsableAPIRenderer",
 ]
 }
 3
institute/urls.py
 from django.contrib import admin
 from django.urls import path, include
 from rest_framework.routers import DefaultRouter
 from api.views import TrainerViewSet, SubjectViewSet, index
 router = DefaultRouter()
 router.register(r"trainer", TrainerViewSet, basename="trainer")
 router.register(r"subject", SubjectViewSet, basename="subject")
 urlpatterns = [
 path("admin/", admin.site.urls),
 path("", index, name="home"), # Front-end page
 path("", include(router.urls)), # REST API endpoints
 ]
 api/models.py
 from django.db import models
 class Subject(models.Model):
 name = models.CharField(max_length=100, unique=True)
 def _str_(self):
 return self.name
 class Trainer(models.Model):
 empId = models.AutoField(primary_key=True)
 name = models.CharField(max_length=100)
 subjects = models.ManyToManyField(Subject, related_name="trainers",
 blank=True)
 def _str_(self):
 return f"{self.name} ({self.empId})"
 api/serializers.py
 from rest_framework import serializers
 from .models import Trainer, Subject
 4
class SubjectSerializer(serializers.ModelSerializer):
 class Meta:
 model = Subject
 fields = ["id", "name"]
 class TrainerSerializer(serializers.ModelSerializer):
 subjects = SubjectSerializer(many=True, read_only=True)
 class Meta:
 model = Trainer
 fields = ["empId", "name", "subjects"]
 class TrainerWriteSerializer(serializers.ModelSerializer):
 subject_ids = serializers.PrimaryKeyRelatedField(
 queryset=Subject.objects.all(), many=True, write_only=True,
 required=False
 )
 class Meta:
 model = Trainer
 fields = ["empId", "name", "subject_ids"]
 def create(self, validated_data):
 subject_ids = validated_data.pop("subject_ids", [])
 trainer = Trainer.objects.create(**validated_data)
 if subject_ids:
 trainer.subjects.set(subject_ids)
 return trainer
 def update(self, instance, validated_data):
 subject_ids = validated_data.pop("subject_ids", None)
 instance.name = validated_data.get("name", instance.name)
 instance.save()
 if subject_ids is not None:
 instance.subjects.set(subject_ids)
 return instance
 api/views.py
 from django.shortcuts import render
 from rest_framework import viewsets
 from rest_framework.decorators import action
 from rest_framework.response import Response
 5
from rest_framework.request import Request
 from .models import Trainer, Subject
 from .serializers import TrainerSerializer, TrainerWriteSerializer,
 SubjectSerializer
 # Front-end home page (plain Django view)
 def index(request):
 # Provide subjects for the add-trainer form dropdown
 subjects = Subject.objects.all().order_by("name")
 return render(request, "index.html", {"subjects": subjects})
 class TrainerViewSet(viewsets.ModelViewSet):
 queryset =
 Trainer.objects.prefetch_related("subjects").all().order_by("empId")
 def get_serializer_class(self):
 if self.action in ["create", "update", "partial_update"]:
 return TrainerWriteSerializer
 return TrainerSerializer
 # GET /trainer/{subject}/topic
 @action(detail=False, methods=["get"], url_path=r"(?P<subject>[^/]+)/topic")
 def by_subject(self, request: Request, subject: str = None):
 trainers = self.get_queryset().filter(subjects_name_iexact=subject)
 data = TrainerSerializer(trainers, many=True).data
 return Response(data)
 class SubjectViewSet(viewsets.ModelViewSet):
 queryset = Subject.objects.all().order_by("name")
 serializer_class = SubjectSerializer
 # GET /subject/{id}  -> subject details + trainers teaching it
 def retrieve(self, request: Request, *args, **kwargs):
 subject = self.get_object()
 trainers = subject.trainers.all().order_by("name")
 payload = {
 "id": subject.id,
 "name": subject.name,
 "trainers": TrainerSerializer(trainers, many=True).data,
 }
 return Response(payload)
 6
templates/index.html
 <!DOCTYPE html>
 <html lang="en">
 <head>
 <meta charset="UTF-8" />
 <meta name="viewport" content="width=device-width, initial-scale=1.0" />
 <title>Institute — Trainers & Subjects</title>
  {% load static %}
 <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
 </head>
 <body>
 <header>
 <h1>Institute — Trainers & Subjects</h1>
 </header>
 <main>
 <section class="card">
 <h2>Add Subject</h2>
 <form id="subject-form">
        {% csrf_token %}
 <input id="subject-name" type="text" placeholder="Subject name"
 required />
 <button type="submit">Add Subject</button>
 </form>
 <div id="subjects-list" class="list"></div>
 </section>
 <section class="card">
 <h2>Add Trainer</h2>
 <form id="trainer-form">
        {% csrf_token %}
 <input id="trainer-name" type="text" placeholder="Trainer name"
 required />
 <label>Subjects</label>
 <select id="trainer-subjects" multiple>
          {% for s in subjects %}
 <option value="{{ s.id }}">{{ s.name }}</option>
          {% endfor %}
 </select>
 <button type="submit">Add Trainer</button>
 </form>
 </section>
 <section class="card">
 <h2>Trainers</h2>
 7
<div class="controls">
 <input id="filter-subject" placeholder="Filter by subject (exact)" />
 <button id="btn-filter">Filter</button>
 <button id="btn-refresh">Refresh</button>
 </div>
 <div id="trainers-list" class="list"></div>
 </section>
 </main>
 <script src="{% static 'js/app.js' %}"></script>
 </body>
 </html>
 static/css/styles.css
 :root {--bg: #0f172a;--card: #111827;--text: #e5e7eb;--muted: #9ca3af;--accent: #4f46e5;
 }
 * { box-sizing: border-box; }
 body {
 margin: 0; font-family: system-ui,-apple-system, Segoe UI, Roboto,
 Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji";
 background: var(--bg); color: var(--text);
 }
 header { padding: 24px 20px; border-bottom: 1px solid #1f2937; }
 main { max-width: 1100px; margin: 24px auto; padding: 0 16px; display: grid;
 grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; }
 .card { background: var(--card); border: 1px solid #1f2937; border-radius:
 16px; padding: 16px; box-shadow: 0 10px 20px rgba(0,0,0,0.2); }
 h1 { margin: 0; font-size: 24px; }
 h2 { margin: 8px 0 12px; font-size: 18px; }
 input, select, button { width: 100%; margin: 8px 0; padding: 10px 12px; border
radius: 10px; border: 1px solid #374151; background: #0b1220; color: var(-
text); }
 button { background: var(--accent); border: none; cursor: pointer; font-weight:
 600; }
 button:hover { opacity: .95; }
 .list { display: grid; gap: 8px; }
 .item { display: flex; align-items: center; justify-content: space-between;
 padding: 10px 12px; background: #0b1220; border: 1px solid #1f2937; border
8
radius: 10px; }
 .controls { display: flex; gap: 8px; }
 .controls input { flex: 1; }
 .badge { display: inline-block; padding: 2px 8px; border-radius: 999px;
 background: #1f2937; color: var(--muted); margin-right: 6px; font-size: 12px; }
 .empty { color: var(--muted); font-style: italic; }
 static/js/app.js
 // CSRF helper from Django docs
 function getCookie(name) {
 let cookieValue = null;
 if (document.cookie && document.cookie !== "") {
 const cookies = document.cookie.split(";");
 for (let i = 0; i < cookies.length; i++) {
 const cookie = cookies[i].trim();
 if (cookie.substring(0, name.length + 1) === (name + '=')) {
 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
 break;
 }
 }
 }
 return cookieValue;
 }
 const csrftoken = getCookie('csrftoken');
 async function api(path, options = {}) {
 const opts = Object.assign({
 headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrftoken },
 credentials: 'same-origin'
 }, options);
 const res = await fetch(path, opts);
 if (!res.ok) throw new Error(await res.text());
 return res.status === 204 ? null : res.json();
 }
 // Subjects
 const subjForm = document.getElementById('subject-form');
 const subjName = document.getElementById('subject-name');
 const subjList = document.getElementById('subjects-list');
 async function loadSubjects() {
 const subs = await api('/subject/');
 subjList.innerHTML = '';
 9
if (!subs.length) {
 subjList.innerHTML = '<div class="empty">No subjects yet.</div>';
 return;
 }
 subs.forEach(s => {
 const div = document.createElement('div');
 div.className = 'item';
 div.innerHTML = <span>${s.name}</span>;
 subjList.appendChild(div);
 });
 }
 subjForm?.addEventListener('submit', async (e) => {
 e.preventDefault();
 await api('/subject/', { method: 'POST', body: JSON.stringify({ name:
 subjName.value }) });
 subjName.value = '';
 await loadSubjects();
 await refreshTrainerSubjects();
 });
 // Trainers
 const trainerForm = document.getElementById('trainer-form');
 const trainerName = document.getElementById('trainer-name');
 const trainerSubjects = document.getElementById('trainer-subjects');
 const trainersList = document.getElementById('trainers-list');
 const filterSubject = document.getElementById('filter-subject');
 async function listTrainers(subject = null) {
 trainersList.innerHTML = '';
 const path = subject ? /trainer/${encodeURIComponent(subject)}/topic/ : '/
 trainer/';
 const data = await api(path);
 if (!data.length) {
 trainersList.innerHTML = '<div class="empty">No trainers found.</div>';
 return;
 }
 data.forEach(t => {
 const div = document.createElement('div');
 div.className = 'item';
 const subjects = (t.subjects || []).map(s => `<span class="badge">${s.name}
 </span>`).join('');
 div.innerHTML = `
      <div>
        <strong>${t.name}</strong> <span class="muted">(ID: ${t.empId})</
 span><br/>
 ${subjects}
      </div>
 10
      <div>
        <button data-id="${t.empId}" class="btn-del">Delete</button>
      </div>`;
 trainersList.appendChild(div);
 });
 document.querySelectorAll('.btn-del').forEach(btn => {
 btn.addEventListener('click', async () => {
 const id = btn.getAttribute('data-id');
 await api(/trainer/${id}/, { method: 'DELETE' });
 await listTrainers(subject);
 });
 });
 }
 async function refreshTrainerSubjects() {
 // Rebuild the multi-select from subjects endpoint (for when new subjects are 
added)
 const subs = await api('/subject/');
 trainerSubjects.innerHTML = '';
 subs.forEach(s => {
 const opt = document.createElement('option');
 opt.value = s.id;
 opt.textContent = s.name;
 trainerSubjects.appendChild(opt);
 });
 }
 trainerForm?.addEventListener('submit', async (e) => {
 e.preventDefault();
 const selected = Array.from(trainerSubjects.selectedOptions).map(o =>
 Number(o.value));
 await api('/trainer/', { method: 'POST', body: JSON.stringify({ name:
 trainerName.value, subject_ids: selected }) });
 trainerName.value = '';
 trainerSubjects.selectedIndex =-1;
 await listTrainers();
 });
 // Filter controls
 const btnFilter = document.getElementById('btn-filter');
 const btnRefresh = document.getElementById('btn-refresh');
 btnFilter?.addEventListener('click', async () => { await
 listTrainers(filterSubject.value.trim() || null); });
 btnRefresh?.addEventListener('click', async () => { filterSubject.value='';
 await listTrainers(); });
 // Initial loads
 11
loadSubjects();
 listTrainers();
 api/admin.py (optional, to manage via admin site)
 from django.contrib import admin
 from .models import Subject, Trainer
 @admin.register(Subject)
 class SubjectAdmin(admin.ModelAdmin):
 list_display = ("id", "name")
 search_fields = ("name",)
 @admin.register(Trainer)
 class TrainerAdmin(admin.ModelAdmin):
 list_display = ("empId", "name")
 search_fields = ("name",)
 filter_horizontal = ("subjects",)
 api/apps.py
 from django.apps import AppConfig
 class ApiConfig(AppConfig):
 default_auto_field = "django.db.models.BigAutoField"
 name = "api"
 api/urls.py (optional; not required when using router in project
 urls)
 from django.urls import path
 # Using project-level router; keep file if you want to add extra non-viewset 
endpoints later.
 urlpatterns = []
 12
How to Run
 1) Create & activate a virtualenv (recommended), then install deps: 
pip install-r requirements.txt
 2) Create DB and run migrations: 
python manage.py makemigrations
 python manage.py migrate
 3) Start the dev server: 
python manage.py runserver
 4) Open the app UI at: 
http://127.0.0.1:8000/
 5) Browse API: - 
POST /trainer/ — add trainer (JSON: 
[1,2] } ) - 
{ "name": "Alice", "subject_ids": 
GET /trainer/ — all trainers - 
DELETE /trainer/{id}/ — remove trainer - 
trainer/{id}/ — trainer by empId - 
GET /
 GET /trainer/{subject}/topic/ — trainers teaching a subject- POST
 /subject/ — add subject (JSON: 
{ "name": "Math" } ) - 
GET /subject/{id}/ — subject details incl. trainers
 GET /subject/ — all subjects 
Swagger-like browsable API is available by default from DRF; just visit the endpoints in the
 browser.
 Notes
 • 
• 
• 
The front-end uses the CSRF token cookie and sends it via 
app.js .
 Static files are served by 
referenced with 
{% static %} .
 X-CSRFToken header automatically in 
runserver in development; CSS/JS live under 
static/ and are
 The custom action path 
GET /trainer/{subject}/topic/ is handled by a ViewSet 
@action
 with a regex 
url_path .
 Happy building! 🛠
 13