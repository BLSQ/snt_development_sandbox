"""Fixture pipeline, added in v0.2.0-test."""

from openhexa.sdk import current_run, pipeline


@pipeline("snt_fixture_pipeline_added")
def snt_fixture_pipeline_added():
    """Do nothing; this pipeline exists only as a release fixture.

    Returns
    -------
    None
    """
    current_run.log_info("fixture pipeline (added in v0.2.0-test)")


if __name__ == "__main__":
    snt_fixture_pipeline_added()
