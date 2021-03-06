# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# Replaced mock values
MOCKED_SUBSCRIPTION_ID = '00000000-0000-0000-0000-000000000000'
MOCKED_TENANT_ID = '00000000-0000-0000-0000-000000000000'

# Configuration environment variable
ENV_COMMAND_COVERAGE = 'AZURE_TEST_COMMAND_COVERAGE'
ENV_LIVE_TEST = 'AZURE_TEST_RUN_LIVE'
ENV_SKIP_ASSERT = 'AZURE_TEST_SKIP_ASSERT'
ENV_TEST_DIAGNOSE = 'AZURE_TEST_DIAGNOSE'
# Keep crime scene (resources) when a test case fails. It is super useful for debugging.
ENV_TEST_NO_CLEANUP_ON_FAIL = 'AZURE_TEST_NO_CLEANUP_ON_FAIL'
