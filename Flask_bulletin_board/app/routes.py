from flask import render_template, redirect, url_for, request
from . import db
from .models import Advertisement
from .forms import AdvertisementForm

def register_routes(app):
    @app.route("/")
    def index():
        ads = Advertisement.query.all()
        return render_template("index.html", ads=ads)

    @app.route("/create", methods=["GET", "POST"])
    def create():
        form = AdvertisementForm()
        if form.validate_on_submit():
            new_ad = Advertisement(
                title=form.title.data,
                description=form.description.data,
                price=form.price.data
            )
            db.session.add(new_ad)
            db.session.commit()
            return redirect(url_for("index"))
        return render_template("create.html", form=form)

    @app.route("/delete/<int:ad_id>")
    def delete(ad_id):
        ad = Advertisement.query.get_or_404(ad_id)
        db.session.delete(ad)
        db.session.commit()
        return redirect(url_for("index"))

    app.add_url_rule("/", view_func=index)
    app.add_url_rule("/create", view_func=create, methods=["GET", "POST"])
    app.add_url_rule("/delete/<int:ad_id>", view_func=delete)
