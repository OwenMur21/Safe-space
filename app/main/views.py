from . import main
from flask import render_template,abort,redirect,url_for,request,abort,flash
from flask_login import login_required, current_user
from ..models import User, Crisis, Commentcrisis, Fam, Commentfam, Health, Commenthealth, Mental, Commentmental
from .forms import PostForm, CommentForm
from profanityfilter import ProfanityFilter
from ..email import mail_message


pf = ProfanityFilter()
pf_custom = ProfanityFilter(custom_censor_list=['die','kufa','mbuzi','mavi','stupid','shonde','fago','gofa','chichi','lezi','ujinga','fala','horny','suck my','lick my','kiss my','balls'])

@main.route('/')
def home():
    """
    Function that renders the home page
    """
    title="Welcome | Safe Space"

    return render_template('home.html', title=title)


@main.route('/about')
@login_required
def about():
    """
    Function that renders the about page
    """
    title="About Us"

    return render_template('about.html')


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
        content = pf_custom.censor(form.content.data) 
        content = pf.censor(content)
        new_crisis=Crisis(content=content,user_id=current_user.id)
        new_crisis.save_crisis()
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
        content = pf_custom.censor(form.content.data) 
        content = pf.censor(content)
        new_fam=Fam(content=content,user_id=current_user.id)
        new_fam.save_Fam()
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
        content = pf_custom.censor(form.content.data) 
        content = pf.censor(content)
        new_depression=Mental(content=content,user_id=current_user.id)
        new_depression.save_mental()
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
        content = pf_custom.censor(form.content.data) 
        content = pf.censor(content)
        new_health=Health(content=content,user_id=current_user.id)
        new_health.save_health()
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
    health.delete_health()
    return redirect(url_for('main.new_health'))


@main.route('/view-crisis/<int:id>', methods=['GET', 'POST'])
@login_required
def view_crisis(id):
    """
    Returns the crisis to be commented on
    """
    the_crisis = Crisis.query.filter_by(id = id).first()
    comments = Commentcrisis.query.filter_by(crisis_id=id).all()
    form=CommentForm()
    if form.validate_on_submit():
        description = pf_custom.censor(form.description.data)
        description = pf.censor(description)
        new_comment=Commentcrisis(description=description,user_id=current_user.id,crisis_id=the_crisis.id)
        new_comment.save_comment()
        return redirect(url_for('.view_crisis',id=id))

  
    return render_template('commentcrisis.html', crisis=the_crisis, comments=comments,form=form)

@main.route('/view-fam/<int:id>', methods=['GET', 'POST'])
@login_required
def view_fam(id):
    """
    Returns the fam to be commented on
    """
    the_fam = Fam.query.filter_by(id = id).first()
    comments = Commentfam.query.filter_by(fam_id=id).all()
    form=CommentForm()
    if form.validate_on_submit():
        description = pf_custom.censor(form.description.data)
        description = pf.censor(description)
        new_comment=Commentfam(description=description,user_id=current_user.id,fam_id=the_fam.id)
        new_comment.save_commentl()
        return redirect(url_for('.view_fam',id=id))
    return render_template('commentfam.html', fam=the_fam, comments=comments, form=form)

@main.route('/view-health/<int:id>', methods=['GET', 'POST'])
@login_required
def view_health(id):
    """
    Returns the health to be commented on
    """
    the_health = Health.query.filter_by(id = id).first()
    comments = Commenthealth.query.filter_by(health_id=id).all()
    form=CommentForm()
    if form.validate_on_submit():
        description = pf_custom.censor(form.description.data)
        description = pf.censor(description)
        new_comment=Commenthealth(description=description,user_id=current_user.id,health_id=the_health.id)
        new_comment.save_commenthealth()
        return redirect(url_for('.view_health',id=id))
    return render_template('commenthealth.html', health=the_health, comments=comments, form=form)

@main.route('/view-mental/<int:id>', methods=['GET', 'POST'])
@login_required
def view_mental(id):
    """
    Returns the mental to be commented on
    """
    the_mental = Mental.query.filter_by(id = id).first()
    comments = Commentmental.query.filter_by(mental_id=id).all()
    form=CommentForm()
    if form.validate_on_submit():
        description = pf_custom.censor(form.description.data)
        description = pf.censor(description)
        new_comment=Commentmental(description=description,user_id=current_user.id,mental_id=the_mental.id)
        new_comment.save_commentmental()
        return redirect(url_for('.view_mental',id=id))
    return render_template('commentmental.html', mental=the_mental, comments=comments, form=form)

@main.route('/delete-comment/<int:id>', methods=['GET', 'POST'])
@login_required
def del_comment(id):
    """
    Function that enables one to delete a comment in crisis
    """
    comment = Commentcrisis.query.filter_by(id=id).first()
    crisis = Crisis.query.filter_by(id = comment.crisis_id).first()
    if comment.user_id != current_user.id:
        abort(403)
    comment.delete_comment()
    return redirect(url_for('.view_crisis',id=crisis.id))


@main.route('/delete-commentl/<int:id>', methods=['GET', 'POST'])
@login_required
def del_commentl(id):
    """
    Function that enables one to delete a comment in fam
    """
    comment = Commentfam.query.filter_by(id=id).first()
    fam = Fam.query.filter_by(id = comment.fam_id).first()
    if comment.user_id != current_user.id:
        abort(403)
    comment.delete_commentl()
    return redirect(url_for('.view_fam',id=fam.id))

@main.route('/delete-commenth/<int:id>', methods=['GET', 'POST'])
@login_required
def del_commenth(id):
    """
    Function that enables one to delete a comment in health
    """
    comment = Commenthealth.query.filter_by(id=id).first()
    health = Health.query.filter_by(id = comment.health_id).first()
    if comment.user_id != current_user.id:
        abort(403)
    comment.delete_commenthealth()
    return redirect(url_for('.view_health',id=health.id))

@main.route('/delete-commentm/<int:id>', methods=['GET', 'POST'])
@login_required
def del_commentm(id):
    """
    Function that enables one to delete a comment in mental
    """
    comment = Commentmental.query.filter_by(id=id).first()
    mental = Mental.query.filter_by(id = comment.mental_id).first()
    if comment.user_id != current_user.id:
        abort(403)
    comment.delete_commentmental()
    return redirect(url_for('.view_mental',id=mental.id))


@main.route('/sos/<int:id>', methods=['GET', 'POST'])
@login_required
def sos(id):
    """
    Function that enables one to send an sos
    """
    user = User.query.filter_by(id=id).first()
    mail_message("Get help don't give up","email/sos", user.email,user = user)
    return redirect(url_for('main.index', user=user))

 