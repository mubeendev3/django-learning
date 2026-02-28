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
14. [Progress Since Last README Update](#progress-since-last-readme-update)

---

## 1. Project Overview

### What This Project Is About

This is a **Django 6.0** learning project: a small multi-page site with a home page, features page, contact form, login page, and a **recipe app** where users can add recipes (name, description, image). It demonstrates the core Django workflow: **models → migrations → views → URLs → templates**, plus **template inheritance**, **form POST handling with redirect**, and **file uploads** (media files).

### What I Was Trying to Learn

- How to create and run a Django project and apps
- Defining models and using migrations to change the database
- Mapping URLs to views and passing data to templates
- Using Django’s template language (loops, conditionals, context)
- **Template inheritance** — a base template with `{% block %}` and child templates that `{% extends "base.html" %}`
- Building forms with CSRF protection and **handling POST** (reading `request.POST`, creating model instances, **redirect** after submit)
- **File uploads** — `request.FILES`, `enctype="multipart/form-data"`, `ImageField`, and serving media in development
- Organizing a project with multiple apps (`home`, `accounts`, **`recipe`**)

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
- **Templates** — HTML with variables, loops, and conditionals; **template inheritance** with `{% extends %}` and `{% block %}`
- **Context** — Passing data from views to templates
- **Forms and CSRF** — Safe POST handling with `{% csrf_token %}`
- **POST handling and redirect** — Check `request.method == "POST"`, read `request.POST` / `request.FILES`, save data, then `redirect()` to avoid double submit
- **Media files** — User-uploaded files (e.g. images) with `MEDIA_ROOT`, `MEDIA_URL`, and serving in DEBUG

### Skills I Practiced

- Creating a project with `django-admin startproject` and apps with `startapp`
- Writing models (`CharField`, `IntegerField`, `EmailField`, `TextField`), then `makemigrations` and `migrate`
- Writing function-based views using `render()` and `HttpResponse()`
- Defining `urlpatterns` and using `path()` and named routes
- Using DTL: `{% for %}`, `{% if %}`, `{{ variable }}`, `{{ forloop.counter }}`, `{% empty %}`, `{% csrf_token %}`, **`{% extends %}`, `{% block %}`, `{% url 'name' %}`**
- **Template inheritance** — one `base.html` (nav, footer, styles), all pages extend it and fill blocks
- Styling pages with custom CSS and Tailwind (CDN)
- **Handling form POST** — read `request.POST` and `request.FILES`, create model instances, `redirect()` after success
- **Serving uploaded images** — `MEDIA_ROOT`, `MEDIA_URL`, and `static()` in `urls.py` when `DEBUG` is True

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
- **Where I used it:** One project `core` (from `django-admin startproject core`), three apps: `home` (main pages), `accounts` (placeholder), and **`recipe`** (recipe form and model).
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
- **Where I used it:** In `core/urls.py`: `''` → `home`, `'success/'` → `success_page`, `'features/'`, `'contact/'`, `'login/'`, **`'recipe/'` → `recipe`**; `'admin/'` for Django admin. When `DEBUG` is True, `urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` so uploaded media files are served.
- **Why it matters:** Clean URLs and one place to change routing; named routes avoid hardcoding paths in templates; media serving in dev is configured in the same file.

### 3.6 Templates and the Django Template Language (DTL)

- **What it is:** **Templates** are HTML files with placeholders and logic. DTL provides `{{ variable }}`, `{% for %}`, `{% if %}`, `{% empty %}`, `{% csrf_token %}`, and built-ins like `forloop.counter`.
- **Where I used it:** `home/templates/`: `base.html` (layout + blocks), `index.html`, `features.html`, `contact.html`, `login.html` (all extend `base.html` and use `{% csrf_token %}` where needed). `recipe/templates/recipes.html` also extends `base.html` and uses DTL for the recipe form.
- **Why it matters:** Separates structure (HTML) from logic; keeps views thin and templates readable; inheritance removes duplication.

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
- **Where I used it:** In `core/settings.py`, `EXTERNAL_APPS = ['accounts', 'home', 'recipe', 'django_extensions']` then `INSTALLED_APPS += EXTERNAL_APPS`.
- **Why it matters:** Unlisted apps are invisible to Django (migrations won’t run, templates won’t be found).

### 3.10 Static Files and Styling

- **What it is:** **Static files** (CSS, JS, images) are served under `STATIC_URL`. Here, CSS is either inline in templates or brought in via Tailwind CDN and custom `<style>`.
- **Where I used it:** Home uses inline CSS and Montserrat; Features, Contact, and Login use Tailwind CDN plus small custom classes (e.g. `.gradient-bg`, `.card-glass`).
- **Why it matters:** Understanding where styles live (inline vs static vs CDN) helps when you later use `collectstatic` and deployment.

### 3.11 Template Inheritance

- **What it is:** A **base template** defines the common layout (e.g. `<head>`, nav, footer) and **blocks** (`{% block title %}`, `{% block content %}`). Child templates use `{% extends "base.html" %}` and override blocks with `{% block content %}...{% endblock %}`.
- **Where I used it:** `home/templates/base.html` has the nav (with `{% url 'home' %}`, `{% url 'features' %}`, etc.), active-link styling via `request.path`, footer, and blocks `title`, `content`, `extra_head`, `extra_js`. All pages (index, features, contact, login, and **recipe’s** `recipes.html`) extend it.
- **Why it matters:** One place to change nav/footer; no duplicated layout; adding a new link (e.g. Recipe) is done once in the base.

### 3.12 File Uploads and Media Files

- **What it is:** **Media files** are user uploads (e.g. images). You set `MEDIA_ROOT` (where files are stored) and `MEDIA_URL` (URL prefix). In views you read files from `request.FILES`; in forms you use `enctype="multipart/form-data"`. For `ImageField`, Django (and Pillow) validate that the file is an image.
- **Where I used it:** Recipe form has `<input type="file" name="recipe_image" accept="image/*">` and `enctype="multipart/form-data"`. View uses `request.FILES.get('recipe_image')` and `Recipe.objects.create(..., recipe_image=recipe_image)`. Model has `ImageField(upload_to='images/recipe')`. In `settings.py`: `MEDIA_ROOT = BASE_DIR / 'media'`, `MEDIA_URL = '/media/'`. In `urls.py`, when `DEBUG` is True, `urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` so uploaded images are served at `/media/`.
- **Why it matters:** POST data alone doesn’t include file contents; you must use `multipart/form-data` and `request.FILES`. Serving media in development is separate from static files.

### 3.13 Redirect After POST

- **What it is:** After successfully processing a POST (e.g. creating a record), return `redirect('url_name')` (or `redirect('/path/')`) instead of rendering the same form again. This avoids “resubmit form?” on refresh and gives a clean GET page.
- **Where I used it:** In `recipe/views.py`, after `Recipe.objects.create(...)`, the view returns `return redirect("/recipe/")` so the user sees the recipe page again as a GET request.
- **Why it matters:** Prevents double submission and follows the “POST/Redirect/GET” pattern.

---

## 4. Features Implemented

### 4.0 Base Template (shared layout)

- **Functionality:** Single layout used by all main pages. Provides nav (logo + links to Home, Features, Contact, Login, **Recipe**), active-link highlighting via `request.path`, footer, Tailwind + Montserrat, and blocks: `title`, `content`, `extra_head`, `extra_js`.
- **Where it lives:** `home/templates/base.html`. All of index, features, contact, login, and recipe’s `recipes.html` use `{% extends "base.html" %}` and fill `{% block content %}` (and optionally `{% block title %}`).
- **Why it matters:** One place to add/change nav links and styling; no duplicated header/footer across pages.

### 4.1 Home Page (`/`)

- **Functionality:** Displays a list of people in a table with columns: No., Name, Age, Can Vote.
- **Logic:** View builds a list of dicts (`people`) and passes it to `index.html`. Template extends `base.html`, loops over `people`, uses `forloop.counter` for the row number, and uses `{% if person.age >= 18 %}` for “Yes”/“No” and red background for under-18.
- **Structure:** Base layout + hero section with table, “Get Started” button to `/success/`.

### 4.2 Success Page (`/success/`)

- **Functionality:** Simple page that returns a plain HTML string via `HttpResponse` (no template).
- **Purpose:** Practice returning a direct response and linking from the home page.

### 4.3 Features Page (`/features/`)

- **Functionality:** Marketing-style grid of six feature cards (Fast & Reliable, Clean Design, Responsive, Secure, Customize, Support).
- **Structure:** Extends `base.html`; responsive grid (`grid-cols-1 sm:grid-cols-2 lg:grid-cols-3`); each card has icon, title, description and hover styles.
- **Tech:** Tailwind CDN, custom `.card-glass` and `.gradient-bg`, Montserrat.

### 4.4 Contact Page (`/contact/`)

- **Functionality:** Contact info (address, email, phone) and a contact form (name, email, subject, message). Form uses `method="post"` and `{% csrf_token %}`; `action="#"` is placeholder until a view handles POST.
- **Structure:** Extends `base.html`; two-column layout on desktop (info cards + form); form has labels, required fields, and a submit button.
- **Tech:** Same Tailwind + glass style as Features/Login.

### 4.5 Login Page (`/login/`)

- **Functionality:** Login form (username/email, password, “Remember me”, “Forgot password?” / “Sign up” links). Form is POST with `{% csrf_token %}`; `action="#"` is placeholder.
- **Structure:** Extends `base.html`; centered card, same styling as Contact/Features.
- **Tech:** Tailwind, `.card-glass`, focus styles on inputs.

### 4.6 Models (Database)

- **Student:** `name` (CharField 100), `age` (IntegerField), `email` (EmailField 254), `address` (TextField, null/blank). No `__str__` in current code; can add for admin.
- **Car:** `car_name` (CharField 100), `max_speed` (IntegerField, default 50), `__str__` returns `car_name`.
- **Recipe** (in `recipe` app): `recipe_name` (CharField 500), `recipe_description` (TextField), `recipe_image` (ImageField, `upload_to='images/recipe'`), `__str__` returns `recipe_name`. **Used in the recipe view** — form POST creates new `Recipe` instances and saves uploaded images to `media/images/recipe/`.
- **Usage:** Student and Car are defined and migrated but not used in views. Recipe is used by the recipe form and view.

### 4.7 Recipe Page (`/recipe/`) — NEW

- **Functionality:** Form to add a recipe: name, description, and image file. On **GET**, the form is shown. On **POST**, the view reads `request.POST` (recipe_name, recipe_description) and `request.FILES` (recipe_image), creates a `Recipe` with `Recipe.objects.create(...)`, then **redirects** to `/recipe/` to avoid resubmit.
- **Structure:** Extends `base.html`; single form with `enctype="multipart/form-data"`, `{% csrf_token %}`, text input, textarea, and file input (`accept="image/*"`). Styling matches other pages (card-glass, Tailwind).
- **Tech:** File upload via `request.FILES`; images stored under `MEDIA_ROOT/images/recipe/` and served at `/media/images/recipe/...` when DEBUG is True.

### 4.8 Django Admin

- **Status:** Admin is enabled (`admin.site.urls`). `home` and `accounts` models are not registered in `admin.py`. You can register `Student`, `Car`, and **`Recipe`** in their respective `admin.py` to manage them via `/admin/`.

---

## 5. Project Structure Explanation

```
django-practice/
├── core/                          # Django project (config + root URLs)
│   ├── core/                      # Project package
│   │   ├── __init__.py
│   │   ├── settings.py            # Main settings (apps, DB, TEMPLATES, MEDIA_ROOT, MEDIA_URL)
│   │   ├── urls.py                # Root URLconf: home + recipe + admin; static(media) when DEBUG
│   │   ├── asgi.py                # ASGI entry for async servers
│   │   └── wsgi.py                # WSGI entry for deployment
│   ├── home/                      # Main app (pages + models)
│   │   ├── migrations/            # Migration files (order matters)
│   │   │   ├── 0001_initial.py … 0004_car_alter_student_name.py
│   │   ├── templates/
│   │   │   ├── base.html          # Shared layout (nav, footer, blocks)
│   │   │   ├── index.html
│   │   │   ├── features.html
│   │   │   ├── contact.html
│   │   │   └── login.html
│   │   ├── admin.py, apps.py, models.py (Student, Car), tests.py, views.py
│   ├── recipe/                    # Recipe app (form + model + file upload)
│   │   ├── migrations/
│   │   │   └── 0001_initial.py    # Recipe model
│   │   ├── templates/
│   │   │   └── recipes.html       # Add-recipe form (extends base.html)
│   │   ├── admin.py, apps.py, models.py (Recipe), tests.py, views.py (recipe view)
│   ├── accounts/                  # Future auth/user app (placeholders)
│   ├── media/                     # User uploads (created at runtime; recipe images go here)
│   │   └── images/recipe/         # ImageField upload_to path
│   ├── manage.py
│   └── db.sqlite3
└── venv/                          # Virtual environment (not in version control)
```

### Important Files

| File | Purpose |
|------|--------|
| `core/settings.py` | INSTALLED_APPS (includes `recipe`), DATABASES, TEMPLATES, **MEDIA_ROOT**, **MEDIA_URL**, etc. |
| `core/urls.py` | Root URL routing (home, recipe, admin); **static(media)** when DEBUG. |
| `home/views.py` | Home page logic; `recipe/views.py` has recipe form GET/POST and redirect. |
| `home/models.py` | Student, Car; **`recipe/models.py`** — Recipe (with ImageField). |
| `home/templates/base.html` | **Base template** (nav with `{% url %}`, active state, blocks). |
| `home/templates/*.html`, `recipe/templates/recipes.html` | Pages extending base; DTL, CSRF. |
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

### 6.8 Base template in `home` app

- **Decision:** Put `base.html` in `home/templates/` so it’s found by any app that uses `{% extends "base.html" %}` (Django searches all INSTALLED_APPS’ `templates/`).
- **Reason:** Home is the “main” app; one base keeps nav/footer consistent. Recipe (and any future app) can extend it without duplicating layout.

### 6.9 Media files and serving in DEBUG

- **Decision:** Set `MEDIA_ROOT = BASE_DIR / 'media'` and `MEDIA_URL = '/media/'`. In `urls.py`, when `DEBUG` is True, append `static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` to `urlpatterns`.
- **Reason:** Uploaded recipe images need to be served; in development Django doesn’t serve MEDIA by default, so this line does it. In production you’d use the server (e.g. nginx) or a CDN.

### 6.10 Explicit recipe view import in urls

- **Decision:** Use `from recipe.views import recipe` (and keep `from home.views import *` or explicit home imports) in `core/urls.py`.
- **Reason:** Clear which view handles `/recipe/`; avoids relying on wildcard import from recipe.

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

### 7.7 ImageField / Pillow (optional dependency)

- **What happened:** After adding `ImageField` to the Recipe model and running `makemigrations`/`migrate`, you might see a warning or error that Pillow is required for ImageField.
- **Why:** Django’s `ImageField` uses Pillow to validate and get dimensions of uploaded images. Without it, basic file storage can still work in some setups, but best practice is to install Pillow.
- **Fix:** Run `pip install Pillow`. Then (if needed) run `makemigrations` and `migrate` again.
- **Learning:** For `ImageField`, add Pillow to your environment (and later to `requirements.txt`).

### 7.8 Template not found for “base.html” from recipe app

- **What happened:** Recipe template does `{% extends "base.html" %}` but Django might not find it if the base lived only in recipe’s templates and was named differently, or if app order was wrong.
- **Why:** With `APP_DIRS` True, Django looks in every app’s `templates/` folder. Putting `base.html` in `home/templates/` (home is in INSTALLED_APPS) makes it available to all apps.
- **Fix:** Keep a single `base.html` in one app (e.g. `home/templates/base.html`) so all apps can extend it. Ensure that app is in `INSTALLED_APPS`.
- **Learning:** Shared templates like base can live in one app and be reused by others; template name is just `"base.html"`, not `"home/base.html"`, so the first app that has `templates/base.html` wins.

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
| `pip install Pillow` | Installs Pillow (required for Django’s `ImageField` to validate images). |
| `python manage.py startapp recipe` | Creates the `recipe` app (already done). |

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

### 9.6 File upload form (recipe)

- **Difficulty:** Getting the browser to send the file and Django to receive it.
- **Approach:** Form must have `enctype="multipart/form-data"`; view reads `request.FILES.get('recipe_image')` and passes it to `Recipe.objects.create(...)`. Set `MEDIA_ROOT` and `MEDIA_URL` and serve media in dev with `static(MEDIA_URL, document_root=MEDIA_ROOT)` in `urls.py`.

---

## 10. Key Learnings

1. **Django is MVT:** Model (data), View (logic + response), Template (presentation). URL routing connects requests to views.
2. **Migrations are mandatory for model changes:** Edit `models.py` → `makemigrations` → `migrate`. Don’t edit the DB by hand.
3. **Context is the bridge:** Views pass a dict to `render()`; template variables are the keys (e.g. `people`).
4. **Template names are resolved per app:** With `APP_DIRS` True, `render(request, 'index.html')` from the `home` app looks in `home/templates/index.html`.
5. **CSRF is required for POST forms:** Always include `{% csrf_token %}` in forms that POST.
6. **Apps must be in INSTALLED_APPS:** Otherwise migrations and template discovery won’t work for that app.
7. **Named URLs are best practice:** Use `name='home'` etc. so you can use `{% url 'home' %}` and `redirect('home')` instead of hardcoding paths. The base template uses `{% url 'home' %}`, `{% url 'recipe' %}`, etc., so adding a new page only requires one nav change.
8. **One project, many apps:** Keeps features (e.g. home vs recipe) separated and reusable.
9. **Template inheritance:** One base template with `{% block %}` and child templates with `{% extends "base.html" %}` removes duplication and keeps nav/footer in one place.
10. **Redirect after POST:** After saving form data, return `redirect('url_name')` so a refresh doesn’t resubmit the form (POST/Redirect/GET).
11. **File uploads need `enctype="multipart/form-data"`** and `request.FILES`; use `MEDIA_ROOT`/`MEDIA_URL` and serve media in dev with `static()` in `urls.py`.

---

## 11. Future Improvements

- **Register models in admin:** In `home/admin.py` register `Student` and `Car`; in `recipe/admin.py` register `Recipe`, so you can manage them via `/admin/`.
- **Use models in views:** Replace the hardcoded `people` list with `Student.objects.all()` (or a filtered queryset) and adjust the template if needed.
- **List recipes on recipe page:** On GET for `/recipe/`, pass `Recipe.objects.all()` (or ordered) to the template and display a list or grid of existing recipes above or below the form.
- **Handle form POST for contact/login:** Add view logic for contact form (and login) that handle `request.method == 'POST'`, validate input, and either save (e.g. to a ContactMessage model) or show errors.
- **Add requirements.txt:** Run `pip freeze > requirements.txt` (include `Pillow` if using ImageField) so others can install with `pip install -r requirements.txt`.
- **Use URL names in templates:** Base template already uses `{% url 'home' %}`, etc.; any remaining hardcoded paths can be switched to `{% url 'name' %}`.
- **Base template:** ✅ Done — `home/templates/base.html` with blocks; all main pages extend it.
- **Static files properly:** Move repeated CSS into `static/css/` and use `{% load static %}`; later add Tailwind build if needed.
- **Tests:** Add unit tests for views (status code, template used, context, redirect after recipe POST) and for models in `home/tests.py`, `recipe/tests.py`, and `accounts/tests.py`.
- **Version control:** Initialize Git if not already; use the project `.gitignore` (e.g. `venv/`, `db.sqlite3`, `media/` if you don’t want uploads in repo, `__pycache__/`, `.env`), and commit the project.

---

## 12. Personal Notes Section

### Quick revision checklist

- **New app:** `python manage.py startapp appname` → add to `INSTALLED_APPS` → create models/views/templates as needed.
- **New model or field change:** Edit `models.py` → `python manage.py makemigrations` → `python manage.py migrate`.
- **New page:** Add view in the right app → add `path()` in `urls.py` (or app urls + `include`) → create template (usually `{% extends "base.html" %}` and `{% block content %}...`) in that app’s `templates/`.
- **Pass data to template:** In the view: `return render(request, 'page.html', {'key': value})`. In the template: `{{ key }}`, `{% for x in key %}`, etc.
- **Form that will POST:** Put `{% csrf_token %}` inside the form; use `method="post"`. For **file uploads** add `enctype="multipart/form-data"`. In the view: `if request.method == 'POST':` → read `request.POST` and `request.FILES` → save (e.g. `Model.objects.create(...)`) → **`return redirect('url_name')`** so refresh doesn’t resubmit.
- **Template not found:** Check that the app is in `INSTALLED_APPS` and that the template path matches: with `APP_DIRS` True it’s `appname/templates/<name_you_passed>.html`. For `base.html`, it’s in `home/templates/base.html` and used by all apps.
- **Serving uploaded files in dev:** In `urls.py`, add `if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` (and set `MEDIA_ROOT`, `MEDIA_URL` in settings).

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
| **Media files** | User-uploaded files; stored in `MEDIA_ROOT`, URL prefix `MEDIA_URL`; in dev often served via `static()` in urls. |
| **Pillow** | Python image library; required by Django’s `ImageField` for image validation/dimensions. |
| **POST/Redirect/GET** | Pattern: form POST → process → redirect to a GET URL so refresh doesn’t resubmit. |

---

## Progress Since Last README Update

- **Recipe app added:** New app `recipe` with `Recipe` model (name, description, image), form in `recipes.html`, and view that handles GET (show form) and POST (create recipe, then redirect to `/recipe/`).
- **Base template:** `home/templates/base.html` created; all main pages (index, features, contact, login, recipes) now extend it. Nav uses `{% url 'name' %}` and highlights active page via `request.path`; Recipe link added.
- **File uploads:** Recipe form uses `enctype="multipart/form-data"` and `<input type="file">`; view uses `request.FILES.get('recipe_image')`; `ImageField(upload_to='images/recipe')`; `MEDIA_ROOT`/`MEDIA_URL` and `static()` in `urls.py` for serving uploads in development.
- **Settings:** `recipe` added to `EXTERNAL_APPS`; `MEDIA_ROOT` and `MEDIA_URL` added.
- **URLs:** `path('recipe/', recipe, name='recipe')` and `urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)` when DEBUG.

---

*This README is a living document. Update it as you add features, fix bugs, or learn new concepts so it stays a useful reference for your future self.*
