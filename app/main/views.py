from . import main
from flask import render_template,abort,redirect,url_for,request,abort,flash
from flask_login import login_required, current_user
from ..models import User, Crisis, Commentcrisis, Fam, Commentfam, Health, Commenthealth, Mental, Commentmental
from .forms import PostForm, CommentForm


@main.route('/')
def home():
    """
    Function that renders the home page
    """
    title="Welcome | Safe Space"

    return render_template('home.html', title=title)


@main.route('/index')
@login_required
def index():
    """
    Function that returns the index which has all the categories
    """

    return render_template('index.html')


@main.route('/identity', methods=['GET', 'POST'])
@login_required
def new_crisis():
    """
    Function that chooses the identity crisis category
    """
    form = PostForm()
    crisises=Crisis.query.all()
    if crisises is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        new_crisis=Crisis(content=content,user_id=current_user.id)
        new_crisis.save_crisis()
        flash('Your post has been posted!')
        return redirect(url_for('.new_crisis'))
  
    return render_template('crisis.html',form=form,crisises=crisises)


@main.route('/fam', methods=['GET', 'POST'])
@login_required
def new_fam():
    """
    Function that chooses the family issues category
    """
    form = PostForm()
    fams=Fam.query.all()
    if fams is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        new_fam=Fam(content=content,user_id=current_user.id)
        new_fam.save_Fam()
        flash('Your post has been posted!')
        return redirect(url_for('.new_fam'))
  

    return render_template('fam.html',form=form, fams=fams)


@main.route('/mental', methods=['GET', 'POST'])
@login_required
def new_depression():
    """
    Function that chooses the depression category
    """
    form = PostForm()
    deps=Mental.query.all()
    if deps is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        new_depression=Mental(content=content,user_id=current_user.id)
        new_depression.save_mental()
        flash('Your post has been posted!')
        return redirect(url_for('.new_depression'))
  

    return render_template('mental.html',form=form,deps=deps)


@main.route('/health', methods=['GET', 'POST'])
@login_required
def new_health():
    """
    Function that chooses the family issues category
    """
    form = PostForm()
    healths=Health.query.all()
    if healths is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        new_health=Health(content=content,user_id=current_user.id)
        new_health.save_health()
        flash('Your post has been posted!')
        return redirect(url_for('.new_health'))
  

    return render_template('health.html',form=form,healths=healths)


@main.route('/delete-crisis/<int:id>', methods=['GET', 'POST'])
@login_required
def del_crisis(id):
    """
    Function that enables one to delete a post from crisis
    """
    crisis = Crisis.query.get_or_404(id)
    if crisis.user_id != current_user.id:
        abort(403)
    crisis.delete_crisis()
    return redirect(url_for('main.new_crisis'))


@main.route('/delete-fam/<int:id>', methods=['GET', 'POST'])
@login_required
def del_fam(id):
    """
    Function that enables one to delete a post from fam
    """
    fam = Fam.query.get_or_404(id)
    if fam.user_id != current_user.id:
        abort(403)
    fam.delete_fam()
    return redirect(url_for('main.new_fam'))


@main.route('/delete-mental/<int:id>', methods=['GET', 'POST'])
@login_required
def del_mental(id):
    """
    Function that enables one to delete a post from mental issues
    """
    mental = Mental.query.get_or_404(id)
    if mental.user_id != current_user.id:
        abort(403)
    mental.delete_mental()
    return redirect(url_for('main.new_depression'))


@main.route('/delete-health/<int:id>', methods=['GET', 'POST'])
@login_required
def del_health(id):
    """
    Function that enables one to delete a post from health
    """
    health = Health.query.get_or_404(id)
    if health.user_id != current_user.id:
        abort(403)
    crisis.delete_health()
    return redirect(url_for('main.new_health'))


@main.route('/view-crisis/<int:id>', methods=['GET', 'POST'])
@login_required
def view_crisis(id):
    """
    Returns the crisis to be commented on
    """
    crisis = Crisis.query.get(id)
    comments = Commentcrisis.get_comments(id)
    return render_template('commentcrisis.html', crisis=crisis, comments=comments, id=id)

@main.route('/view-fam/<int:id>', methods=['GET', 'POST'])
@login_required
def view_fam(id):
    """
    Returns the fam to be commented on
    """
    fam = Fam.query.get(id)
    comments = Commentfam.get_commentsl(id)
    return render_template('commentfam.html', fam=fam, comments=comments, id=id)

@main.route('/view-health/<int:id>', methods=['GET', 'POST'])
@login_required
def view_health(id):
    """
    Returns the crisis to be commented on
    """
    health = Health.query.get(id)
    comments = Commenthealth.get_commenthealth(id)
    return render_template('commenthealth.html', health=health, comments=comments, id=id)

@main.route('/view-mental/<int:id>', methods=['GET', 'POST'])
@login_required
def view_mental(id):
    """
    Returns the crisis to be commented on
    """
    mental = Mental.query.get(id)
    comments = Commentmental.get_commentmental(id)
    return render_template('commentmental.html', mental=mental, comments=comments, id=id)

