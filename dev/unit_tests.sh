#!/bin/bash

TEST_MODE=1 mamba specs
UNITTESTS_RETCODE=$?
exit $UNITTESTS_RETCODE