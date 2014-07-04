from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker


def db(request):
    """every request will have a session associated with it. and will
    automatically rollback if there's any exception in dealing with
    the request
    """
    maker = request.registry.dbmaker
    session = maker()

    def cleanup(request):
        if request.exception is not None:
            session.rollback()
        else:
            session.commit()
        session.close()

    request.add_finished_callback(cleanup)

    return session

        
def config_static(config):
    config.add_static_view('static', 'static', cache_max_age=3600)


def config_jinja2(config):
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')
    config.add_jinja2_search_path('templates', name='.html')


def config_db(config, settings):
    # configure database with variables sqlalchemy.*
    engine = engine_from_config(settings, prefix="sqlalchemy.")
    config.registry.dbmaker = sessionmaker(bind=engine)

    # add db session to request
    config.add_request_method(db, reify=True)


def config_routes(config):
    config.add_route('home', '/')
    config.scan()

    
def main(global_config, **settings):
    config = Configurator(settings=settings)
    config_static(config)
    config_jinja2(config)
    config_db(config, settings)
    config_routes(config)
    return config.make_wsgi_app()
