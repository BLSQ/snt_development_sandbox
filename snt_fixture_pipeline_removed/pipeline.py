"""Fixture pipeline, present in v0.1.0-test and removed in v0.2.0-test."""

from openhexa.sdk import current_run, pipeline


@pipeline("snt_fixture_pipeline_removed")
def snt_fixture_pipeline_removed():
    """Do nothing; this pipeline exists only as a release fixture.

    Returns
    -------
    None
    """
    current_run.log_info("fixture pipeline (removed in v0.2.0-test)")


if __name__ == "__main__":
    snt_fixture_pipeline_removed()
