# Django Practice — Learning Notes & Project Documentation

A structured learning journal and technical reference for this Django practice project. Use this README to recall what you learned, what you built, and how you solved problems.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Learning Objectives](#2-learning-objectives)
3. [Concepts Learned](#3-concepts-learned)
4. [Features Implemented](#4-features-implemented)
5. [Project Structure Explanation](#5-project-structure-explanation)
6. [Technical Decisions](#6-technical-decisions)
7. [Errors Faced and Solutions](#7-errors-faced-and-solutions)
8. [Terminal Commands Used](#8-terminal-commands-used)
9. [Challenges Faced](#9-challenges-faced)
10. [Key Learnings](#10-key-learnings)
11. [Future Improvements](#11-future-improvements)
12. [Personal Notes Section](#12-personal-notes-section)
13. [Glossary](#13-glossary)

---

## 1. Project Overview

### What This Project Is About

This is a **Django 6.0** learning project: a small multi-page site with a home page, features page, contact form, and login page. It demonstrates the core Django workflow: **models → migrations → views → URLs → templates**, plus basic form handling and styling.

### What I Was Trying to Learn

- How to create and run a Django project and apps
- Defining models and using migrations to change the database
- Mapping URLs to views and passing data to templates
- Using Django’s template language (loops, conditionals, context)
- Building simple forms with CSRF protection
- Organizing a project with multiple apps (`home`, `accounts`)

### Technologies Used

| Technology | Purpose |
|------------|--------|
| **Python** | Backend language |
| **Django 6.0.2** | Web framework (MVT, ORM, admin, auth) |
| **SQLite** | Default database (no extra setup) |
| **HTML / CSS** | Templates and styling |
| **Django Template Language (DTL)** | Dynamic content in templates |
| **Tailwind CSS** (CDN) | Utility-first CSS on Features, Contact, Login |
| **Google Fonts (Montserrat)** | Typography |

### Tools Used

- **Cursor** — Code editor and AI-assisted development
- **Terminal / PowerShell** — Running `manage.py` commands
- **Virtual environment (`venv`)** — Isolated Python and Django install
- **Django Extensions** — Extra management commands (e.g. `shell_plus`)

---

## 2. Learning Objectives

### Concepts I Was Trying to Learn

- **Django project vs app** — One project, multiple apps
- **Models and ORM** — Define data, let Django create tables
- **Migrations** — Track and apply schema changes safely
- **Views** — Functions that handle requests and return responses
- **URL routing** — Map URLs to views (and optional `name` for reverse lookup)
- **Templates** — HTML with variables, loops, and conditionals
- **Context** — Passing data from views to templates
- **Forms and CSRF** — Safe POST handling with `{% csrf_token %}`

### Skills I Practiced

- Creating a project with `django-admin startproject` and apps with `startapp`
- Writing models (`CharField`, `IntegerField`, `EmailField`, `TextField`), then `makemigrations` and `migrate`
- Writing function-based views using `render()` and `HttpResponse()`
- Defining `urlpatterns` and using `path()` and named routes
- Using DTL: `{% for %}`, `{% if %}`, `{{ variable }}`, `{{ forloop.counter }}`, `{% empty %}`, `{% csrf_token %}`
- Styling pages with custom CSS and Tailwind (CDN)
- Keeping a consistent layout (nav, footer, gradient, cards) across pages

### Problems I Tried to Solve

- How to show a list of people on the home page with “Can Vote” based on age
- How to add optional fields (`null=True`, `blank=True`) and remove fields via migrations
- How to add a second model (`Car`) and keep migrations in order
- How to make the site responsive and visually consistent
- How to protect forms with CSRF for future backend handling

---

## 3. Concepts Learned

### 3.1 Django Project and Apps

- **What it is:** A **project** is the main config (settings, root URLs). **Apps** are reusable modules (models, views, templates) that you plug into the project.
- **Where I used it:** One project `core` (from `django-admin startproject core`), two apps: `home` (main pages) and `accounts` (placeholder for user-related features).
- **Why it matters:** Keeps code organized and reusable; each app can have its own models, views, and templates.

### 3.2 Models and the ORM

- **What it is:** **Models** are Python classes that define database tables. Django’s ORM turns model fields into columns and lets you query with Python (e.g. `Student.objects.all()`).
- **Where I used it:** In `home/models.py`: `Student` (name, age, email, address) and `Car` (car_name, max_speed). `Student` uses `CharField`, `IntegerField`, `EmailField`, `TextField`; `Car` uses `default=50` and `__str__` for admin/list display.
- **Why it matters:** You define data once in code; Django handles SQL and migrations.

### 3.3 Migrations

- **What it is:** **Migrations** are files that describe schema changes (add/remove/alter tables and columns). You create them with `makemigrations` and apply them with `migrate`.
- **Where I used it:** `home/migrations/`: initial `Student` → alter `address` to optional → remove `file` → add `Car` and alter `Student.name` to `max_length=100`.
- **Why it matters:** Safe, repeatable way to change the database without writing raw SQL; required when you change models.

### 3.4 Views (Function-Based)

- **What it is:** **Views** are callables (here, functions) that receive an `HttpRequest` and return an `HttpResponse`. They can render a template with context or return plain HTML.
- **Where I used it:** In `home/views.py`: `home()` (list of people + `index.html`), `success_page()` (plain `HttpResponse`), `features()`, `contact()`, `login_page()` (each renders one template).
- **Why it matters:** Views are where request handling and “what to show” live; they connect URLs to templates and data.

### 3.5 URL Routing

- **What it is:** **URLconf** maps URL paths to views. `path('url/', view_function, name='name')` lets you refer to the URL by name (e.g. in templates or `redirect()`) and keeps URLs in one place.
- **Where I used it:** In `core/urls.py`: `''` → `home`, `'success/'` → `success_page`, `'features/'`, `'contact/'`, `'login/'` each to a view; `'admin/'` for Django admin.
- **Why it matters:** Clean URLs and one place to change routing; named routes avoid hardcoding paths in templates.

### 3.6 Templates and the Django Template Language (DTL)

- **What it is:** **Templates** are HTML files with placeholders and logic. DTL provides `{{ variable }}`, `{% for %}`, `{% if %}`, `{% empty %}`, `{% csrf_token %}`, and built-ins like `forloop.counter`.
- **Where I used it:** `home/templates/`: `index.html` (people table, loop, age check for “Can Vote”), `features.html`, `contact.html`, `login.html` (all use `{% csrf_token %}` in forms).
- **Why it matters:** Separates structure (HTML) from logic; keeps views thin and templates readable.

### 3.7 Context

- **What it is:** **Context** is a dict passed from a view to a template. Keys become template variable names (e.g. `people` in `index.html`).
- **Where I used it:** `home()` builds `people` (list of dicts with name/age) and passes it as `render(request, 'index.html', {"people": people})`.
- **Why it matters:** This is how views send data to templates; no context means no dynamic data.

### 3.8 CSRF Protection

- **What it is:** **CSRF (Cross-Site Request Forgery)** protection ensures POST requests come from your own forms. Django requires a token in forms and checks it in middleware.
- **Where I used it:** Contact and Login forms include `{% csrf_token %}`; when you add POST handling in the view, Django will validate the token.
- **Why it matters:** Prevents other sites from submitting forms on behalf of your users; required for secure forms.

### 3.9 Apps and INSTALLED_APPS

- **What it is:** Every app must be listed in `INSTALLED_APPS` so Django loads its models, templates, and static files. You can group “external” or “local” apps for clarity.
- **Where I used it:** In `core/settings.py`, `EXTERNAL_APPS = ['accounts', 'home', 'django_extensions']` then `INSTALLED_APPS += EXTERNAL_APPS`.
- **Why it matters:** Unlisted apps are invisible to Django (migrations won’t run, templates won’t be found).

### 3.10 Static Files and Styling

- **What it is:** **Static files** (CSS, JS, images) are served under `STATIC_URL`. Here, CSS is either inline in templates or brought in via Tailwind CDN and custom `<style>`.
- **Where I used it:** Home uses inline CSS and Montserrat; Features, Contact, and Login use Tailwind CDN plus small custom classes (e.g. `.gradient-bg`, `.card-glass`).
- **Why it matters:** Understanding where styles live (inline vs static vs CDN) helps when you later use `collectstatic` and deployment.

---

## 4. Features Implemented

### 4.1 Home Page (`/`)

- **Functionality:** Displays a list of people in a table with columns: No., Name, Age, Can Vote.
- **Logic:** View builds a list of dicts (`people`) and passes it to `index.html`. Template loops over `people`, uses `forloop.counter` for the row number, and uses `{% if person.age >= 18 %}` for “Yes”/“No” and red background for under-18.
- **Structure:** Nav (logo + links), hero section with table, “Get Started” button to `/success/`, footer.

### 4.2 Success Page (`/success/`)

- **Functionality:** Simple page that returns a plain HTML string via `HttpResponse` (no template).
- **Purpose:** Practice returning a direct response and linking from the home page.

### 4.3 Features Page (`/features/`)

- **Functionality:** Marketing-style grid of six feature cards (Fast & Reliable, Clean Design, Responsive, Secure, Customize, Support).
- **Structure:** Same nav/footer as other pages; responsive grid (`grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`); each card has icon, title, description and hover styles.
- **Tech:** Tailwind CDN, custom `.card-glass` and `.gradient-bg`, Montserrat.

### 4.4 Contact Page (`/contact/`)

- **Functionality:** Contact info (address, email, phone) and a contact form (name, email, subject, message). Form uses `method="post"` and `{% csrf_token %}`; `action="#"` is placeholder until a view handles POST.
- **Structure:** Two-column layout on desktop (info cards + form); form has labels, required fields, and a submit button.
- **Tech:** Same Tailwind + glass style as Features/Login.

### 4.5 Login Page (`/login/`)

- **Functionality:** Login form (username/email, password, “Remember me”, “Forgot password?” / “Sign up” links). Form is POST with `{% csrf_token %}`; `action="#"` is placeholder.
- **Structure:** Centered card, same nav/footer and styling as Contact/Features.
- **Tech:** Tailwind, `.card-glass`, focus styles on inputs.

### 4.6 Models (Database)

- **Student:** `name` (CharField 100), `age` (IntegerField), `email` (EmailField 254), `address` (TextField, null/blank). No `__str__` in current code; can add for admin.
- **Car:** `car_name` (CharField 100), `max_speed` (IntegerField, default 50), `__str__` returns `car_name`.
- **Usage:** Models are defined and migrated; they are not yet used in views (e.g. no listing of students/cars on a page). Ready for admin registration and future views.

### 4.7 Django Admin

- **Status:** Admin is enabled (`admin.site.urls`), but `home` and `accounts` models are not registered in `admin.py`. You can register `Student` and `Car` in `home/admin.py` to manage them via `/admin/`.

---

## 5. Project Structure Explanation

```
django-practice/
├── core/                          # Django project (config + root URLs)
│   ├── core/                      # Project package
│   │   ├── __init__.py
│   │   ├── settings.py            # Main settings (apps, DB, templates, etc.)
│   │   ├── urls.py                # Root URLconf: routes to home views + admin
│   │   ├── asgi.py                # ASGI entry for async servers
│   │   └── wsgi.py                # WSGI entry for deployment
│   ├── home/                      # Main app (pages + models)
│   │   ├── migrations/            # Migration files (order matters)
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_alter_student_address.py
│   │   │   ├── 0003_remove_student_file.py
│   │   │   └── 0004_car_alter_student_name.py
│   │   ├── templates/             # Templates (DTL)
│   │   │   ├── index.html
│   │   │   ├── features.html
│   │   │   ├── contact.html
│   │   │   └── login.html
│   │   ├── __init__.py
│   │   ├── admin.py               # Register models for admin (currently empty)
│   │   ├── apps.py                # App config (HomeConfig)
│   │   ├── models.py              # Student, Car
│   │   ├── tests.py               # Placeholder tests
│   │   └── views.py               # home, success_page, features, contact, login_page
│   ├── accounts/                  # Future auth/user app
│   │   ├── admin.py, apps.py, models.py, tests.py, views.py  # Mostly placeholders
│   ├── manage.py                  # CLI: runserver, migrate, makemigrations, etc.
│   └── db.sqlite3                 # SQLite DB (created after migrate)
└── venv/                          # Virtual environment (not in version control)
```

### Important Files

| File | Purpose |
|------|--------|
| `core/settings.py` | INSTALLED_APPS, DATABASES, TEMPLATES, SECRET_KEY, DEBUG, etc. |
| `core/urls.py` | Root URL routing; includes admin and home views. |
| `home/views.py` | All page logic: data preparation and template rendering. |
| `home/models.py` | Student and Car model definitions. |
| `home/templates/*.html` | Page layout and DTL (variables, loops, CSRF). |
| `manage.py` | Entry point for Django commands (runserver, migrate, makemigrations, createsuperuser). |

---

## 6. Technical Decisions

### 6.1 SQLite

- **Decision:** Use default SQLite (`db.sqlite3` in project directory).
- **Reason:** No install or config; good for learning and local dev. Django abstracts the DB, so switching to PostgreSQL/MySQL later is mainly a settings change.

### 6.2 EXTERNAL_APPS in settings

- **Decision:** Separate `INSTALLED_APPS` into built-in apps and `EXTERNAL_APPS` (accounts, home, django_extensions), then `INSTALLED_APPS += EXTERNAL_APPS`.
- **Reason:** Clear split between Django core and project-specific/third-party apps; easier to scan and maintain.

### 6.3 Function-based views (FBVs)

- **Decision:** Use simple functions in `home/views.py` instead of class-based views (CBVs).
- **Reason:** Few URLs and little logic; FBVs are straightforward to read and debug when learning.

### 6.4 Root URLconf only (no app-level urls.py)

- **Decision:** All routes defined in `core/urls.py`; no `include('home.urls')`.
- **Reason:** Few routes; one file is enough. For larger projects, splitting with `include()` per app is better.

### 6.5 Tailwind via CDN

- **Decision:** Use Tailwind from CDN on Features, Contact, Login; Home uses custom CSS.
- **Reason:** Quick styling without build step; good for practice. For production, a build step or static Tailwind is better for size and caching.

### 6.6 Django Extensions

- **Decision:** Add `django_extensions` to INSTALLED_APPS.
- **Reason:** Extra commands like `shell_plus` (shell with models pre-imported) and others useful for development and learning.

### 6.7 Hardcoded data in home view

- **Decision:** People list is defined in code, not from the database.
- **Reason:** Focus on flow (view → context → template); later you can replace with `Student.objects.all()` or similar.

---

## 7. Errors Faced and Solutions

### 7.1 Model changes not applied / “No migrations to apply” but table wrong

- **What happened:** After changing a model (e.g. adding `null=True, blank=True` to `address`, or removing `file`), the database or admin didn’t reflect it.
- **Why:** Migrations had not been created or applied.
- **Fix:** Run `python manage.py makemigrations` then `python manage.py migrate`. Check that the correct app is in `INSTALLED_APPS`.
- **Learning:** Every model change that affects the DB needs a migration; migrations are the single source of truth for schema.

### 7.2 Removing a model field

- **What happened:** Needed to remove the `file` field from `Student` (see migration `0003_remove_student_file`).
- **Why:** Decided the field wasn’t needed; Django doesn’t remove columns by itself.
- **Fix:** Delete the field from `models.py`, run `makemigrations`; Django generates `RemoveField`. Then `migrate`.
- **Learning:** Migrations can remove columns; data in that column is lost unless you write a data migration.

### 7.3 Template not found (e.g. `index.html`)

- **What happened:** Django raised “TemplateDoesNotExist” for `index.html` or similar.
- **Why:** Template path or `APP_DIRS`/`DIRS` was wrong. With `APP_DIRS: True`, Django looks in each app’s `templates/` folder; it does **not** look for `home/index.html` unless the template name is `home/index.html` or you have a `templates/home/` subfolder. For `render(request, 'index.html')` it looks for `home/templates/index.html` when the view is in `home`.
- **Fix:** Put templates in `home/templates/` and use names like `'index.html'` from the `home` app’s views. If you use `'home/index.html'`, then create `home/templates/home/index.html`.
- **Learning:** With `APP_DIRS` True, each app’s `templates/` is in the search path; template name is relative to that.

### 7.4 CSRF verification failed (when you add form POST handling)

- **What happened:** After submitting a form, Django returns “CSRF verification failed” or similar.
- **Why:** Form didn’t include `{% csrf_token %}` or the view didn’t use the correct request method (e.g. not checking `request.method == 'POST'` or not using `RequestContext`).
- **Fix:** In the template, put `{% csrf_token %}` inside the `<form>`. In the view, use `render()` (which uses RequestContext) for the response that contains the form. For POST, process the form and then redirect or re-render with errors.
- **Learning:** All POST forms must send the CSRF token; Django middleware checks it automatically.

### 7.5 Import error: “cannot import name 'X' from 'home.views'”

- **What happened:** After adding a new view, visiting its URL caused an import error.
- **Why:** In `core/urls.py` you use `from home.views import *`. If the view name doesn’t match the one in `path()`, or there’s a typo, the import fails.
- **Fix:** Ensure the function name in `home/views.py` matches the name used in `urls.py` (e.g. `login_page`). Prefer explicit imports: `from home.views import home, success_page, features, contact, login_page`.
- **Learning:** Wildcard imports can hide missing or renamed names; explicit imports make dependencies clear.

### 7.6 Migration dependency order

- **What happened:** Adding a new model (e.g. `Car`) and changing another (e.g. `Student.name` max_length) in one go; migration order or dependencies caused confusion.
- **Why:** Migrations have a dependency chain (e.g. 0004 depends on 0003). Creating multiple migrations in one `makemigrations` run can bundle several operations; splitting or ordering can matter when you have multiple apps.
- **Fix:** Run `makemigrations` after each logical change if you want separate steps; resolve conflicts with `makemigrations --merge` only if Django says so. Here, 0004 correctly depends on 0003.
- **Learning:** Migrations are sequential; don’t delete or renumber them by hand; use `showmigrations` to see applied state.

---

## 8. Terminal Commands Used

| Command | What it does |
|--------|----------------|
| `python -m venv venv` | Creates a virtual environment in the `venv` folder. |
| `venv\Scripts\activate` (Windows) | Activates the virtual environment so `python` and `pip` use it. |
| `pip install django` | Installs Django in the current environment. |
| `pip install django-extensions` | Installs Django Extensions (e.g. shell_plus). |
| `django-admin startproject core .` or `django-admin startproject core` | Creates a new Django project named `core` (with or without current dir as project root). |
| `python manage.py startapp home` | Creates a new app named `home` inside the project. |
| `python manage.py runserver` | Starts the development server (default http://127.0.0.1:8000/). |
| `python manage.py makemigrations` | Creates migration files for model changes (in each app that has changes). |
| `python manage.py migrate` | Applies all pending migrations to the database. |
| `python manage.py showmigrations` | Lists migrations and whether they are applied. |
| `python manage.py createsuperuser` | Prompts to create an admin user for the Django admin site. |
| `python manage.py shell` | Opens a Python shell with Django and project settings loaded. |
| `python manage.py shell_plus` | (With django_extensions) Opens shell with models already imported. |
| `python manage.py check` | Checks for common project/config issues without running the server. |

---

## 9. Challenges Faced

### 9.1 Understanding the request–response flow

- **Difficulty:** Knowing where to put logic: URL vs view vs template.
- **Approach:** Reminded myself: URL chooses the view, view prepares data and picks the template, template renders HTML. Kept logic in the view and only presentation in the template.

### 9.2 Making address optional on Student

- **Difficulty:** Making `address` optional without breaking the DB.
- **Approach:** Set `null=True, blank=True` on `TextField`, then `makemigrations` and `migrate`. Migration 0002 applied this change.

### 9.3 Deciding when to use template vs HttpResponse

- **Difficulty:** When to use `render()` vs `HttpResponse()`.
- **Approach:** Use `render()` for full HTML pages (with templates and context); use `HttpResponse()` for very simple or non-HTML responses (e.g. “Success” snippet). Success page was kept minimal on purpose.

### 9.4 Keeping styling consistent across pages

- **Difficulty:** Home had custom CSS; other pages needed similar look.
- **Approach:** Reused the same gradient, Montserrat, and card style; on Features/Contact/Login used Tailwind plus small custom classes (e.g. `.card-glass`, `.gradient-bg`) so the look and feel match.

### 9.5 Forms without backend yet

- **Difficulty:** Contact and Login forms need to look and behave like real forms but don’t process POST yet.
- **Approach:** Used `method="post"`, `{% csrf_token %}`, and `action="#"` so the structure is correct. When you add POST handling, point `action` to a URL and add a view that checks `request.method` and processes the form.

---

## 10. Key Learnings

1. **Django is MVT:** Model (data), View (logic + response), Template (presentation). URL routing connects requests to views.
2. **Migrations are mandatory for model changes:** Edit `models.py` → `makemigrations` → `migrate`. Don’t edit the DB by hand.
3. **Context is the bridge:** Views pass a dict to `render()`; template variables are the keys (e.g. `people`).
4. **Template names are resolved per app:** With `APP_DIRS` True, `render(request, 'index.html')` from the `home` app looks in `home/templates/index.html`.
5. **CSRF is required for POST forms:** Always include `{% csrf_token %}` in forms that POST.
6. **Apps must be in INSTALLED_APPS:** Otherwise migrations and template discovery won’t work for that app.
7. **Named URLs are best practice:** Use `name='home'` etc. so you can use `{% url 'home' %}` and `redirect('home')` instead of hardcoding paths.
8. **One project, many apps:** Keeps features (e.g. home vs accounts) separated and reusable.

---

## 11. Future Improvements

- **Register models in admin:** In `home/admin.py`, register `Student` and `Car` so you can manage them via `/admin/`.
- **Use models in views:** Replace the hardcoded `people` list with `Student.objects.all()` (or a filtered queryset) and adjust the template if needed.
- **Handle form POST:** Add URL and view for contact form (and login) that handle `request.method == 'POST'`, validate input, and either save (e.g. to a ContactMessage model) or show errors.
- **Add requirements.txt:** Run `pip freeze > requirements.txt` so others (and future you) can install the same packages with `pip install -r requirements.txt`.
- **Use URL names in templates:** Replace hrefs like `/features/` with `{% url 'features' %}` for maintainability.
- **Base template:** Extract common nav/footer/head into a `base.html` and use `{% extends "base.html" %}` and `{% block content %}` in each page to avoid duplication.
- **Static files properly:** Move repeated CSS into `static/css/` and use `{% load static %}` and `<link href="{% static 'css/style.css' %}">`; later add Tailwind build if needed.
- **Tests:** Add unit tests for views (status code, template used, context) and for models in `home/tests.py` and `accounts/tests.py`.
- **Version control:** Initialize Git, add a `.gitignore` (e.g. `venv/`, `db.sqlite3`, `__pycache__/`, `.env`), and commit the project.

---

## 12. Personal Notes Section

### Quick revision checklist

- **New app:** `python manage.py startapp appname` → add to `INSTALLED_APPS` → create models/views/templates as needed.
- **New model or field change:** Edit `models.py` → `python manage.py makemigrations` → `python manage.py migrate`.
- **New page:** Add view in the right app → add `path()` in `urls.py` (or app urls + `include`) → create template in that app’s `templates/`.
- **Pass data to template:** In the view: `return render(request, 'page.html', {'key': value})`. In the template: `{{ key }}`, `{% for x in key %}`, etc.
- **Form that will POST:** Put `{% csrf_token %}` inside the form; use `method="post"` and set `action` to the URL that will handle it. In the view, check `if request.method == 'POST':` and process, then redirect or re-render with errors.
- **Template not found:** Check that the app is in `INSTALLED_APPS` and that the template path matches: with `APP_DIRS` True it’s `appname/templates/<name_you_passed>.html`.

### Mental model

- **Request:** User hits a URL → Django matches it in `urlpatterns` → calls the view with `request`.
- **View:** Gets data (from DB or hardcoded), puts it in context, calls `render(request, 'template.html', context)`.
- **Template:** Receives context as variables; outputs HTML with `{{ }}` and `{% %}`.
- **Response:** Django returns the rendered HTML (or other response) to the browser.

### Useful Django docs (for later)

- [Django 6.0 docs](https://docs.djangoproject.com/en/6.0/)
- Tutorial (part 1–7): project setup, models, admin, views, templates, forms.
- Topics: Writing views, URL dispatcher, Templates, Working with forms, Migrations.

---

## 13. Glossary

| Term | Meaning |
|------|--------|
| **App** | A Django component (module) with its own models, views, templates, etc., listed in `INSTALLED_APPS`. |
| **Context** | A dictionary passed from a view to a template; keys become template variable names. |
| **CSRF** | Cross-Site Request Forgery; Django uses a token in forms and middleware to block forged requests. |
| **DTL** | Django Template Language; the syntax for variables, tags, and filters in templates. |
| **FBV** | Function-Based View; a view implemented as a Python function. |
| **Migration** | A file describing a schema change (add/remove/alter tables/columns); applied with `migrate`. |
| **MVT** | Model–View–Template; Django’s way of structuring data, logic, and presentation. |
| **ORM** | Object-Relational Mapping; using Python objects (models) and methods instead of writing SQL. |
| **Project** | The top-level Django config (settings, root URLs); contains one or more apps. |
| **URLconf** | URL configuration; the `urlpatterns` list that maps URLs to views. |
| **View** | A callable that receives a request and returns a response; here, functions in `views.py`. |
| **WSGI/ASGI** | Interfaces for deploying Django (e.g. with Gunicorn or Uvicorn). |

---

*This README is a living document. Update it as you add features, fix bugs, or learn new concepts so it stays a useful reference for your future self.*
