import datetime
import json_format

graph_apps_data = [
    {
        "id": "03215ee3-5e3d-42d6-a0b2-ad6425ac156f",
        "displayName": "TripActions",
        "passwordCredentials": [],
    },
    {
        "id": "057b3063-b7aa-4d7b-b6cb-f310c7a886fa",
        "displayName": "Processed Videos Prod",
        "passwordCredentials": [],
    },
    {
        "id": "060e7aa4-741a-4821-973d-567149436d8c",
        "displayName": "AWS DataRA_2",
        "passwordCredentials": [],
    },
    {
        "id": "07e03357-b478-48c0-ae0f-56232b87de15",
        "displayName": "OpsGenie SSO",
        "passwordCredentials": [],
    },
    {
        "id": "07f5b679-d558-4492-b46c-0a7f1e271f39",
        "displayName": "PaperCut User Sync",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "PaperCut User Sync Secret",
                "endDateTime": "2025-01-29T12:00:18.901Z",
                "hint": "QqT",
                "keyId": "76c641f3-9983-44d4-b5c8-eeb7fb88e8cd",
                "secretText": None,
                "startDateTime": "2023-01-30T12:00:18.901Z",
            }
        ],
    },
    {
        "id": "095d4107-a758-4321-84ed-fd38576d070f",
        "displayName": "Manufacturing Prod",
        "passwordCredentials": [],
    },
    {
        "id": "0bff9738-7cea-481e-b987-a9bee44d36e3",
        "displayName": "1Password Business",
        "passwordCredentials": [],
    },
    {
        "id": "0cdf0df5-ae68-405f-8a4e-cbc13d6c9ec7",
        "displayName": "CQ - eQMS",
        "passwordCredentials": [],
    },
    {
        "id": "0d427e99-c263-40d6-beed-9fbf43602666",
        "displayName": "DevOps Prod",
        "passwordCredentials": [],
    },
    {
        "id": "0f51b8c8-5c99-47b3-a39f-167f6084d194",
        "displayName": "jupyterhub_telemetry",
        "passwordCredentials": [
            {
                "customKeyIdentifier": "agBoAF8AdABlAGwAZQBtAGUAdAByAHkA",
                "displayName": None,
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": None,
                "keyId": "3277e7ab-fcde-481e-9347-7e80c440526d",
                "secretText": None,
                "startDateTime": "2018-05-08T14:44:30.8242222Z",
            }
        ],
    },
    {
        "id": "0f97a1cd-05c6-4b49-b01b-67db87d904d5",
        "displayName": "SAS Academy",
        "passwordCredentials": [],
    },
    {
        "id": "0fc63972-e402-47ca-b577-c1063ff5d63d",
        "displayName": "Lacework",
        "passwordCredentials": [],
    },
    {
        "id": "11748c9b-8e90-4a86-92e7-b8a2153fcf9b",
        "displayName": "Asana",
        "passwordCredentials": [],
    },
    {
        "id": "12866684-ec24-48a8-bf7a-3831b38c7c95",
        "displayName": "SharePoint Online Client Extensibility Web Application Principal Helper",
        "passwordCredentials": [],
    },
    {
        "id": "151e7b70-c13a-45fd-8cc7-ddbf2f6d1586",
        "displayName": "Report Phishing",
        "passwordCredentials": [],
    },
    {
        "id": "19dba9e2-34e3-42fb-a466-a8416a5ce96a",
        "displayName": "Dataloop",
        "passwordCredentials": [],
    },
    {
        "id": "1a0a0c08-01d5-4b41-8fd6-09706f1928a9",
        "displayName": "CMR Portal Prod",
        "passwordCredentials": [],
    },
    {
        "id": "1df09b68-3a4b-4e46-aac7-7d601c72f8a9",
        "displayName": "Netsuite",
        "passwordCredentials": [],
    },
    {
        "id": "1e5458fe-7032-4fd6-ac9e-7afcc631f723",
        "displayName": "Klue",
        "passwordCredentials": [],
    },
    {
        "id": "1ef11152-ddb1-42cb-9cc8-eec8a5f6faf2",
        "displayName": "Forsta",
        "passwordCredentials": [],
    },
    {
        "id": "1f887961-01db-4fcf-8c52-01329f3e29d2",
        "displayName": "Meraki",
        "passwordCredentials": [],
    },
    {
        "id": "1fc719e0-85c8-4f45-8a01-3e3128838048",
        "displayName": "Netsuite - Sandbox Environment",
        "passwordCredentials": [],
    },
    {
        "id": "202fdfba-88e6-49fc-b93f-d9fede04feb8",
        "displayName": "PALMA",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "PALMA secret 27-09-2022",
                "endDateTime": "2023-09-27T13:06:20.875Z",
                "hint": "scM",
                "keyId": "5e242b5b-6c04-47b5-9a93-d40b23abb4d0",
                "secretText": None,
                "startDateTime": "2022-09-27T13:06:20.875Z",
            },
            {
                "customKeyIdentifier": None,
                "displayName": "PALMA secret",
                "endDateTime": "2022-09-17T14:03:44.8Z",
                "hint": "P1_",
                "keyId": "79b0cb77-958e-4193-8111-366e07500148",
                "secretText": None,
                "startDateTime": "2021-09-17T14:03:44.8Z",
            },
        ],
    },
    {
        "id": "2030887f-f320-40cc-b785-41707a20a97a",
        "displayName": "Miro (formerly RealtimeBoard)",
        "passwordCredentials": [],
    },
    {
        "id": "20b33fa7-c733-4fa1-8f24-5f6abc3178b5",
        "displayName": "cmrcofensereporter",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Generated by App Service",
                "endDateTime": "2031-05-19T11:29:33.195Z",
                "hint": "FAj",
                "keyId": "c544248c-f662-45b9-b2b1-19daccb14f6b",
                "secretText": None,
                "startDateTime": "2021-05-19T11:29:33.195Z",
            }
        ],
    },
    {
        "id": "23bfc774-8bea-4bbb-8346-5457f4d3b6a8",
        "displayName": "ReadCube Papers",
        "passwordCredentials": [],
    },
    {
        "id": "24343116-212a-4c51-a0ec-a39e0f95ef54",
        "displayName": "Grammarly",
        "passwordCredentials": [],
    },
    {
        "id": "256d65b5-f820-4e59-8d8d-bbdad2aa6032",
        "displayName": "IT Prod",
        "passwordCredentials": [],
    },
    {
        "id": "298bc752-d9ec-4aae-b478-c2dc0b422ef1",
        "displayName": "cmr-data-app-1",
        "passwordCredentials": [],
    },
    {
        "id": "2c0b3078-0310-40ee-a51c-ecb416187557",
        "displayName": "People",
        "passwordCredentials": [],
    },
    {
        "id": "2e6b0c6f-6214-412f-8ed6-97e9e0ae236b",
        "displayName": "M-Files Test",
        "passwordCredentials": [],
    },
    {
        "id": "2ea66401-b046-469a-9c69-384574daddcb",
        "displayName": "AWS Product Support Dev",
        "passwordCredentials": [],
    },
    {
        "id": "2f7d9eb3-dd8b-47e4-9b35-b523f1de9c9a",
        "displayName": "AWS DataRA_3",
        "passwordCredentials": [],
    },
    {
        "id": "3014af66-58c3-4a9c-a084-0bed86d87eb0",
        "displayName": "Analytic Strategy Sandbox",
        "passwordCredentials": [],
    },
    {
        "id": "30c4ae7d-5702-49bf-af81-6f3f3f0ea145",
        "displayName": "Portal Dev",
        "passwordCredentials": [],
    },
    {
        "id": "32a7919a-4e68-4835-9e9c-716a80ba2712",
        "displayName": "cmrscheduler",
        "passwordCredentials": [],
    },
    {
        "id": "32cfddfc-3e86-4fbb-9ff3-2801f51130c8",
        "displayName": "SharePoint Versius System State Tracker",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Secret",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "UBK",
                "keyId": "0a9cef9e-5c07-4ea0-a37e-a55c09bd2b50",
                "secretText": None,
                "startDateTime": "2020-06-18T13:18:14.774Z",
            }
        ],
    },
    {
        "id": "344194d6-aef1-47a2-b396-662a8026cbb4",
        "displayName": "AL Dev",
        "passwordCredentials": [],
    },
    {
        "id": "35b7fd9c-a58e-4bf8-b434-ef2d09274ba6",
        "displayName": "LicensecheckMSGraph",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Licenses",
                "endDateTime": "2024-07-17T23:00:00Z",
                "hint": "3ls",
                "keyId": "07a0d925-2e5f-41ee-adf1-9092d69650c6",
                "secretText": None,
                "startDateTime": "2022-07-18T13:09:37.832Z",
            }
        ],
    },
    {
        "id": "3656a7e4-1072-4f48-bfc8-697749decec2",
        "displayName": "AWS MES-Dev",
        "passwordCredentials": [],
    },
    {
        "id": "37741ece-5d54-429b-98fc-cf5ba55b319e",
        "displayName": "Auth0 production SAML",
        "passwordCredentials": [],
    },
    {
        "id": "37db7ff2-75b2-44e5-8de4-0564be4492ad",
        "displayName": "WP Engine User Portal",
        "passwordCredentials": [],
    },
    {
        "id": "3844f87b-6006-4fda-9af5-b8fcc80ce10f",
        "displayName": "Databricks",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "OpenIDSecret",
                "endDateTime": "2023-07-01T12:00:00.513Z",
                "hint": "6p.",
                "keyId": "5af158d0-5184-4f5f-94bf-452bb95dff7c",
                "secretText": None,
                "startDateTime": "2021-07-01T12:00:14.959Z",
            }
        ],
    },
    {
        "id": "3a0de6f7-7e27-48ac-a7ff-ccc003883d14",
        "displayName": "Medispend(Sandbox)",
        "passwordCredentials": [],
    },
    {
        "id": "3c4a91d9-5071-4a3c-ab59-d68b29675922",
        "displayName": "CMR Surgical Auth Service",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Password uploaded on Tue Jun 09 2020",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "~l9",
                "keyId": "9ec2a0ca-c5d0-42be-af5e-b0d5b3f09a51",
                "secretText": None,
                "startDateTime": "2020-06-09T14:09:32.171Z",
            }
        ],
    },
    {
        "id": "3cd5527f-3c3a-4fa7-a9b3-8790a92b5e03",
        "displayName": "Lacework SA Audit",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Lacework Secret",
                "endDateTime": "2023-11-18T15:21:59.473Z",
                "hint": "Ioh",
                "keyId": "a88c4454-7198-4bab-9b39-81c32bb769f7",
                "secretText": None,
                "startDateTime": "2022-11-18T15:21:59.473Z",
            }
        ],
    },
    {
        "id": "435f1fec-15ab-45e9-8612-f4fc72a2fd8d",
        "displayName": "Procedure Finder - Testing enviroment",
        "passwordCredentials": [],
    },
    {
        "id": "43df3f17-53e6-4f52-b715-ee20988d1428",
        "displayName": "IT Backups",
        "passwordCredentials": [],
    },
    {
        "id": "43f69b9b-69f3-439d-a36d-403e2db1dbad",
        "displayName": "Video Services Prod",
        "passwordCredentials": [],
    },
    {
        "id": "4493fe1a-570f-4b51-85f5-2c964818dae7",
        "displayName": "DSO Research & Development",
        "passwordCredentials": [],
    },
    {
        "id": "456a5217-4a28-4f36-9d07-0a02dafde2fe",
        "displayName": "M Files Dev",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Password uploaded on Wed Sep 21 2022",
                "endDateTime": "2024-09-21T13:52:08.374Z",
                "hint": "EKq",
                "keyId": "7f0adcf6-8f64-460f-8591-18e2927d7fc9",
                "secretText": None,
                "startDateTime": "2022-09-21T13:52:08.374Z",
            },
            {
                "customKeyIdentifier": None,
                "displayName": "ClientSecret",
                "endDateTime": "2022-09-09T14:15:39.648Z",
                "hint": "Io~",
                "keyId": "1b6d0215-149b-43e2-861b-0e8cb9d35732",
                "secretText": None,
                "startDateTime": "2020-09-09T14:16:16.556Z",
            },
        ],
    },
    {
        "id": "4a26b6fa-d3a6-4bbf-9aaa-d7abfdc416f4",
        "displayName": "Sumo Logic",
        "passwordCredentials": [],
    },
    {
        "id": "4a6ca9c3-7e73-4029-8607-aaf89a1099a6",
        "displayName": "Envoy",
        "passwordCredentials": [],
    },
    {
        "id": "4a872fbd-9c25-499c-bdd4-009077270927",
        "displayName": "My Ruby App",
        "passwordCredentials": [],
    },
    {
        "id": "4c21d63b-714f-48f2-9dec-a31d14c922e5",
        "displayName": "Shareworks Production Participant",
        "passwordCredentials": [],
    },
    {
        "id": "4c7a35cd-0e3d-4fc8-b927-ff5608f8ac6b",
        "displayName": "iHASCO Training",
        "passwordCredentials": [],
    },
    {
        "id": "4d5abacf-3355-41e4-956e-400041a15255",
        "displayName": "DevOps Staging",
        "passwordCredentials": [],
    },
    {
        "id": "4d670659-bf54-4fc1-9d95-2fc6c2946119",
        "displayName": "Production Software",
        "passwordCredentials": [],
    },
    {
        "id": "50004d29-c4e3-4271-95a6-89cf9bd73e4b",
        "displayName": "Kantega SSO for Confluence",
        "passwordCredentials": [],
    },
    {
        "id": "50dab33e-7a76-4415-b334-135540fdaf57",
        "displayName": "M-FilesProd",
        "passwordCredentials": [],
    },
    {
        "id": "50edfe21-ee16-4de6-89d2-04dd3a2b83c8",
        "displayName": "Raw Videos Prod",
        "passwordCredentials": [],
    },
    {
        "id": "5146f784-f4c9-45d2-a049-e61261b815a2",
        "displayName": "ContactsSync",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": None,
                "endDateTime": "2099-12-31T12:00:00Z",
                "hint": "byq",
                "keyId": "7bebce84-e253-48be-a617-b3caf2da0ae7",
                "secretText": None,
                "startDateTime": "2018-06-19T09:15:41.1631286Z",
            }
        ],
    },
    {
        "id": "528905d3-5daa-41dc-9bd1-999b39d4fba1",
        "displayName": "Salesforce PreProd",
        "passwordCredentials": [],
    },
    {
        "id": "52c4e159-5c14-4c25-b9e5-6c06bdd685d5",
        "displayName": "Docusign",
        "passwordCredentials": [],
    },
    {
        "id": "54678aa4-0742-441f-a09e-1c826d5d2a2a",
        "displayName": "CMR Portal Sandbox",
        "passwordCredentials": [],
    },
    {
        "id": "548eb82f-73dd-4602-b6bf-404b3400c1df",
        "displayName": "TrainingSite - HowToMoodle",
        "passwordCredentials": [],
    },
    {
        "id": "54d0be5c-3147-46f2-8da6-b0852426090c",
        "displayName": "Video Services Staging",
        "passwordCredentials": [],
    },
    {
        "id": "550c2b94-4e00-42a8-916f-1651621469f3",
        "displayName": "Assure",
        "passwordCredentials": [],
    },
    {
        "id": "55176bcc-bcc0-410f-b1e5-08257a3a16ef",
        "displayName": "AL Prod",
        "passwordCredentials": [],
    },
    {
        "id": "5628bf61-a12c-400a-8f73-dae0869d7c45",
        "displayName": "Docusign (Demo)",
        "passwordCredentials": [],
    },
    {
        "id": "57485d22-0a4d-47e4-b5ae-2f6efd139cb0",
        "displayName": "SharePoint Online Client Extensibility Web Application Principal",
        "passwordCredentials": [
            {
                "customKeyIdentifier": "dy3Il80nEUC4jFSLFe5avQ==",
                "displayName": None,
                "endDateTime": "2070-10-30T11:51:07.2141677Z",
                "hint": None,
                "keyId": "896e84a5-b362-4e5b-b633-7cf3b1380f44",
                "secretText": None,
                "startDateTime": "2020-10-30T11:51:07.2141677Z",
            }
        ],
    },
    {
        "id": "58e1d70e-473d-4cd4-921b-4d9de92fdb4f",
        "displayName": "Delete this",
        "passwordCredentials": [],
    },
    {
        "id": "5980e7ec-ebf8-473d-8f36-31b598d72f2b",
        "displayName": "CMR Salesforce",
        "passwordCredentials": [],
    },
    {
        "id": "599ab9b4-eee9-468f-8167-99e8a8ae0783",
        "displayName": "ITGuardDuty",
        "passwordCredentials": [],
    },
    {
        "id": "5a8bab1a-e5cb-4701-a555-1132d52786dd",
        "displayName": "StackOverFlow",
        "passwordCredentials": [],
    },
    {
        "id": "5ace8df8-f01e-4b2f-8f3b-01efffd89384",
        "displayName": "TSheets",
        "passwordCredentials": [],
    },
    {
        "id": "5af2cd45-b7b1-451d-889c-f869f7f792a6",
        "displayName": "Jira OAuth 2.0",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Jira email this issue addon secret",
                "endDateTime": "2025-01-31T16:40:24.848Z",
                "hint": "Lb_",
                "keyId": "c3020d30-356a-4f3b-893f-6de370679ca7",
                "secretText": None,
                "startDateTime": "2023-02-01T16:40:24.848Z",
            },
            {
                "customKeyIdentifier": None,
                "displayName": "Jira OAuth 2.0",
                "endDateTime": "2024-10-19T14:00:20.759Z",
                "hint": "GS3",
                "keyId": "f745c605-55f7-4669-b9d6-4eedc63bc79a",
                "secretText": None,
                "startDateTime": "2022-10-19T14:00:20.759Z",
            },
        ],
    },
    {
        "id": "5b2ac9ce-1c16-4186-9934-1d84947e8dfb",
        "displayName": "VC Backup",
        "passwordCredentials": [],
    },
    {
        "id": "5eca1fef-39dc-4eda-843a-a9f51bdb61f0",
        "displayName": "Showpad",
        "passwordCredentials": [],
    },
    {
        "id": "5f5f36b1-74bd-45ea-93a1-48d161202b9b",
        "displayName": "Processed Videos Staging",
        "passwordCredentials": [],
    },
    {
        "id": "5f6ea5d4-0832-4a3b-9517-3ca7ef7e2bcc",
        "displayName": "certificates_secrets_expiry",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "secret to be used by Lambda to get information",
                "endDateTime": "2025-02-15T12:17:57.335Z",
                "hint": "ss1",
                "keyId": "e0a2c090-b8a5-443e-ae03-2bb41d046bbb",
                "secretText": None,
                "startDateTime": "2023-02-16T12:17:57.335Z",
            }
        ],
    },
    {
        "id": "62af4cb8-2f8c-477f-aec1-5d7ae9417bd5",
        "displayName": "MediSpend",
        "passwordCredentials": [],
    },
    {
        "id": "62d15cdc-8c14-40d5-8df1-3cb6fb14fed9",
        "displayName": "Assure Testing Enviroment - To be removed confirm with RD",
        "passwordCredentials": [],
    },
    {
        "id": "65489a7f-84f4-4ee1-b309-9fc1e9b4f1b1",
        "displayName": "Brandmaster",
        "passwordCredentials": [],
    },
    {
        "id": "656d518b-b531-45cf-b1a6-bf6300de83cb",
        "displayName": "AWS - SDS videos",
        "passwordCredentials": [],
    },
    {
        "id": "66271f8a-149a-41af-92d1-06099a882816",
        "displayName": "Skedda",
        "passwordCredentials": [],
    },
    {
        "id": "67c65d87-a891-4d42-a11d-4f3c91720f10",
        "displayName": "Mimecast Personal Portal",
        "passwordCredentials": [],
    },
    {
        "id": "6896a48a-b8f3-4766-b6db-888a8c294eeb",
        "displayName": "Raw Videos Dev",
        "passwordCredentials": [],
    },
    {
        "id": "6a295b91-94d4-4699-b4c4-8efb7c96fbdf",
        "displayName": "Analytic Strategy Dev",
        "passwordCredentials": [],
    },
    {
        "id": "6b099c44-7363-40d4-8dfd-1264ac5a8365",
        "displayName": "Auth0 SAML Integration DEV",
        "passwordCredentials": [],
    },
    {
        "id": "6b77941f-980c-4bde-a40d-dfc3c45847a4",
        "displayName": "Test federation thing",
        "passwordCredentials": [],
    },
    {
        "id": "6e9e88ef-e6b7-4eb0-ac26-83ac0585551f",
        "displayName": "Glint",
        "passwordCredentials": [],
    },
    {
        "id": "6f2f7da8-40ad-4d69-a7c4-67ee72fdb116",
        "displayName": "MFiles Test",
        "passwordCredentials": [],
    },
    {
        "id": "71f765f8-3389-47cd-9439-c4a24fa86f74",
        "displayName": "CQ - eQMS Partial Sandbox",
        "passwordCredentials": [],
    },
    {
        "id": "7201115a-6d22-4af2-8e80-f1037f325271",
        "displayName": "AccessIdentity",
        "passwordCredentials": [],
    },
    {
        "id": "7552a04f-edec-4da9-96fa-b068e1347324",
        "displayName": "GitLab",
        "passwordCredentials": [],
    },
    {
        "id": "78be9831-a427-4577-9c4a-4f21b64a1cf1",
        "displayName": "Add_Users_to_Groups_script",
        "passwordCredentials": [],
    },
    {
        "id": "798eddd9-25fc-42ae-a42e-7daaa3af19aa",
        "displayName": "cmr-data-app-3",
        "passwordCredentials": [],
    },
    {
        "id": "79bca0c9-9521-4bb0-b836-a2886d023fbd",
        "displayName": "People",
        "passwordCredentials": [],
    },
    {
        "id": "7a610e0b-1f03-4d66-805b-efb397d15fcd",
        "displayName": "Video Services Dev",
        "passwordCredentials": [],
    },
    {
        "id": "7ac9e185-8e5e-439e-a785-a9086d181cb7",
        "displayName": "Panorama",
        "passwordCredentials": [],
    },
    {
        "id": "7f5faba5-65c2-426b-917a-8d5e6b1e1f40",
        "displayName": "CMR Boomi",
        "passwordCredentials": [],
    },
    {
        "id": "7fe9d1e7-0141-441f-bf17-b16a451e8a9b",
        "displayName": "VersiusCloud Gitlab",
        "passwordCredentials": [
            {
                "customKeyIdentifier": "bQBhAGkAbgA=",
                "displayName": None,
                "endDateTime": "2019-08-17T12:57:19.893Z",
                "hint": None,
                "keyId": "a104c15e-b4f4-46f3-8df2-0befbbd24804",
                "secretText": None,
                "startDateTime": "2018-08-17T12:57:34.3612871Z",
            }
        ],
    },
    {
        "id": "80bea49a-1c5f-4833-a7e1-f8f06779cc45",
        "displayName": "JIRA Datacenter Kantega SSO",
        "passwordCredentials": [],
    },
    {
        "id": "80ff916d-dff9-4a78-b20b-22e6b695615d",
        "displayName": "Auth0 Staging SAML",
        "passwordCredentials": [],
    },
    {
        "id": "82242c18-415a-4c7e-a38a-bdbba1c6d677",
        "displayName": "StatusPage",
        "passwordCredentials": [],
    },
    {
        "id": "823e0410-1aed-47c6-9a39-21c77d09cd7d",
        "displayName": "BIPI Dev",
        "passwordCredentials": [],
    },
    {
        "id": "846c9f4c-2837-4590-b709-f55b624e301c",
        "displayName": "FUTEK-CSV-Autotransfer",
        "passwordCredentials": [],
    },
    {
        "id": "85491a2d-5047-42cd-b926-c161b243e711",
        "displayName": "CMR Amazon Cognito",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "cognito",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "KlF",
                "keyId": "7bbf6301-54da-43f9-9fc0-89ed9d5f7bd0",
                "secretText": None,
                "startDateTime": "2019-09-12T13:36:35.947Z",
            }
        ],
    },
    {
        "id": "86546851-c8a9-48d2-888e-49cfefb2a127",
        "displayName": "Shareworks Admin",
        "passwordCredentials": [],
    },
    {
        "id": "871d895b-be10-408d-9a9f-4bb86ddb2e8b",
        "displayName": "InfosecUserSigninLogs",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Logs",
                "endDateTime": "2024-06-08T12:28:18.321Z",
                "hint": "qjj",
                "keyId": "b4604808-505a-433e-a44b-1707702e3ac3",
                "secretText": None,
                "startDateTime": "2022-06-08T12:28:18.321Z",
            }
        ],
    },
    {
        "id": "872fbbd5-b1c3-4812-afa7-b08e38a15afa",
        "displayName": "StackOverflow",
        "passwordCredentials": [],
    },
    {
        "id": "878b82ce-e4e8-4806-ba68-16f0f77d24af",
        "displayName": "Paul_test",
        "passwordCredentials": [
            {
                "customKeyIdentifier": "cABhAHMAcwB3AG8AcgBkAA==",
                "displayName": None,
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": None,
                "keyId": "28cf16a7-35fc-495e-8761-00106966c5d4",
                "secretText": None,
                "startDateTime": "2018-09-27T21:58:47.8768112Z",
            }
        ],
    },
    {
        "id": "87a9a26d-165b-43dc-a3b0-04c47130a7e0",
        "displayName": "Frontify",
        "passwordCredentials": [],
    },
    {
        "id": "87d5709e-277a-4e3b-bd50-053e68674598",
        "displayName": "AWS - Technology",
        "passwordCredentials": [],
    },
    {
        "id": "880056e8-b227-4e18-ac05-94fdf64aac51",
        "displayName": "AWS Cognito Employee Pool Sandbox",
        "passwordCredentials": [],
    },
    {
        "id": "8844fe2a-23e2-4401-b130-ef323d816416",
        "displayName": "test",
        "passwordCredentials": [],
    },
    {
        "id": "89455857-f337-4c83-aab0-bb5e9e37a95f",
        "displayName": "IT Services",
        "passwordCredentials": [],
    },
    {
        "id": "89bbe308-aef8-4502-8ac9-db3e7a743ffb",
        "displayName": "Greenhouse Recruitment Platform ",
        "passwordCredentials": [],
    },
    {
        "id": "8c0e439d-9cba-442e-a44d-921453201d4b",
        "displayName": "Auth",
        "passwordCredentials": [],
    },
    {
        "id": "8ec87008-50a6-4b98-bd4c-17d9bd437f33",
        "displayName": "Veeam Backup for Microsoft Office 365",
        "passwordCredentials": [],
    },
    {
        "id": "8f5c5ff8-8b25-4328-872d-1ba3e9d9231c",
        "displayName": "Azure AD Domain Services Sync",
        "passwordCredentials": [],
    },
    {
        "id": "90fd00c9-46c5-42a3-b4d3-20a5614d8cc7",
        "displayName": "AWS Cognito Employee Pool Sandbox",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "aws cognito cmr portal test",
                "endDateTime": "2020-05-23T14:41:31.964Z",
                "hint": "7KT",
                "keyId": "791c72ec-a185-4825-b20a-bc652db433bd",
                "secretText": None,
                "startDateTime": "2019-05-23T14:41:48.063Z",
            }
        ],
    },
    {
        "id": "94882a92-1400-4d82-b7d7-4f428f1c2555",
        "displayName": "InTune Jamf CA",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Jamf App ID",
                "endDateTime": "2020-09-06T12:07:32.226Z",
                "hint": "cAU",
                "keyId": "c1659561-ab2d-48e3-be06-58a89e097767",
                "secretText": None,
                "startDateTime": "2019-09-06T12:07:47.667Z",
            }
        ],
    },
    {
        "id": "95946674-f697-4e74-9ec8-23a12f8c2e67",
        "displayName": "IT Dev",
        "passwordCredentials": [],
    },
    {
        "id": "96b956d1-c48f-46a4-8608-6371105a0503",
        "displayName": "Confluence Datacentre Kantega SSO",
        "passwordCredentials": [],
    },
    {
        "id": "981921e6-2592-4215-80de-0d1612b875a2",
        "displayName": "ATR Main",
        "passwordCredentials": [],
    },
    {
        "id": "9872fb38-2435-4ec4-b676-8b61b937ff9f",
        "displayName": "Strategic Analytics Dev Apps",
        "passwordCredentials": [],
    },
    {
        "id": "9a4c29d9-09a8-40df-8e38-98cf01841892",
        "displayName": "ADONIS",
        "passwordCredentials": [],
    },
    {
        "id": "9a781419-215b-4b91-ae22-d1a3c601ccc4",
        "displayName": "Kantega SSO",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Password uploaded on Fri Sep 20 2019",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "ICU",
                "keyId": "989bfca2-a6f9-46d1-90b9-4e7a8466c9f3",
                "secretText": None,
                "startDateTime": "2019-09-20T14:42:41.536Z",
            }
        ],
    },
    {
        "id": "9af5e9e0-269c-49ea-ba23-7f473b77d15d",
        "displayName": "P2P Server",
        "passwordCredentials": [],
    },
    {
        "id": "9c6c96e7-5cb9-4185-b061-1da4f625cd98",
        "displayName": "CMR Amazon Cognito (Dev)",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "cognito",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": ".dh",
                "keyId": "49934366-0b0c-4b42-a2f1-982d0901685b",
                "secretText": None,
                "startDateTime": "2019-09-12T13:35:34.568Z",
            }
        ],
    },
    {
        "id": "9ca25a1d-5801-491a-840b-22c55ca197c8",
        "displayName": "VC Staging",
        "passwordCredentials": [],
    },
    {
        "id": "9e544e5a-f236-4f3e-88d3-29c467739198",
        "displayName": "IT Pet Server",
        "passwordCredentials": [],
    },
    {
        "id": "a0535d71-c3cc-4523-81e1-81ec400b8329",
        "displayName": "DSO Interviews",
        "passwordCredentials": [],
    },
    {
        "id": "a2edd318-87de-49d3-929b-1b2ad62641ef",
        "displayName": "CMR Surgical Auth Service (Dev)",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Password uploaded on Fri Jun 19 2020",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "27M",
                "keyId": "693e283a-c53f-4687-9900-f2748788963a",
                "secretText": None,
                "startDateTime": "2020-06-19T15:58:36.363Z",
            }
        ],
    },
    {
        "id": "a39bf119-723b-47c2-a9e6-5151db1bbcbe",
        "displayName": "PaulOneDriveTest",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": None,
                "endDateTime": "2099-12-31T12:00:00Z",
                "hint": "yzn",
                "keyId": "f0f1d6a8-642b-4f00-8663-410a44750ee1",
                "secretText": None,
                "startDateTime": "2018-06-02T11:06:09.7223282Z",
            }
        ],
    },
    {
        "id": "a49297a4-663a-4558-8db1-f56659445bb3",
        "displayName": "IVideos",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "india app",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "gdF",
                "keyId": "b215d494-be6d-4dc0-926f-869d9f1954b3",
                "secretText": None,
                "startDateTime": "2019-05-23T06:33:06.95Z",
            }
        ],
    },
    {
        "id": "a529494d-a619-4234-bd6c-9212171c5e35",
        "displayName": "Jamf Connect",
        "passwordCredentials": [],
    },
    {
        "id": "a6511386-a2dd-4224-9ff6-e2ba89093b48",
        "displayName": "M Files Dev",
        "passwordCredentials": [],
    },
    {
        "id": "a6fce192-3197-4b20-ada9-e9b8e3efe695",
        "displayName": "10,000ft",
        "passwordCredentials": [],
    },
    {
        "id": "a7c769f4-9a7d-4de7-85a9-a2d76ab58203",
        "displayName": "Video Safe Haven Staging",
        "passwordCredentials": [],
    },
    {
        "id": "a7ed7a21-eab4-4522-883b-a43d743b7c84",
        "displayName": "Showpad - DO NO USE - DELETE AFTER 16/02/2022",
        "passwordCredentials": [
            {
                "customKeyIdentifier": "QQBrAGUAeQA=",
                "displayName": None,
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": None,
                "keyId": "4ee2eda2-ac12-481f-b8b9-e05b5f7049af",
                "secretText": None,
                "startDateTime": "2019-01-18T16:39:23.3569408Z",
            }
        ],
    },
    {
        "id": "a9af3378-ff13-4a47-a723-c530c74568f2",
        "displayName": "CMR Portal authentication",
        "passwordCredentials": [],
    },
    {
        "id": "abeefac3-d6c0-4e87-a4c4-d7f0b8fcde25",
        "displayName": "VC ProServe",
        "passwordCredentials": [],
    },
    {
        "id": "ac009a6c-10e6-4808-bc31-1779df94654e",
        "displayName": "Procedure Finder - Europe",
        "passwordCredentials": [],
    },
    {
        "id": "ad0c4683-1877-486d-a263-6b6a016d85fa",
        "displayName": "LastPass",
        "passwordCredentials": [],
    },
    {
        "id": "ad8d6b01-2abe-4ebd-8a17-f0613739b2c7",
        "displayName": "CMR Portal Staging",
        "passwordCredentials": [],
    },
    {
        "id": "af06face-1595-4367-b9d4-6f747655b805",
        "displayName": "data_sharepoint_api_access",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "sharepoint_api_access",
                "endDateTime": "2024-06-22T09:49:26.105Z",
                "hint": "3ox",
                "keyId": "063109a9-c5ed-42ed-be06-188da40e1c83",
                "secretText": None,
                "startDateTime": "2022-06-22T09:49:26.105Z",
            }
        ],
    },
    {
        "id": "aff171f4-2887-40b7-8552-88480019756d",
        "displayName": "LogicGate",
        "passwordCredentials": [],
    },
    {
        "id": "b12906be-d54e-40b2-ae94-3fca0d77b2fa",
        "displayName": "Raw Videos Staging",
        "passwordCredentials": [],
    },
    {
        "id": "b4636dfb-5d89-4251-bcb8-a2d026ac1c8a",
        "displayName": "Data DevOps",
        "passwordCredentials": [],
    },
    {
        "id": "b519c18e-51b0-4acb-96c0-f3c38875f37d",
        "displayName": "CMR Amazon Cognito (Staging)",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "cognito",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "DUj",
                "keyId": "513f37d8-38dc-48ad-a6f2-436026091369",
                "secretText": None,
                "startDateTime": "2019-09-12T13:36:17.946Z",
            }
        ],
    },
    {
        "id": "b7e91473-2108-4a57-a17a-b029215ce308",
        "displayName": "FVR APP",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "FVR Client",
                "endDateTime": "2023-12-16T13:11:42.144Z",
                "hint": "xqS",
                "keyId": "326dcdb4-b063-4c0b-bed9-9f293f6aaa8c",
                "secretText": None,
                "startDateTime": "2021-12-16T13:11:42.144Z",
            }
        ],
    },
    {
        "id": "b8ae4521-f992-40a9-81e5-4cef356e1d4d",
        "displayName": "Databricks",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Databricks",
                "endDateTime": "2023-06-03T13:56:31.375Z",
                "hint": "mE7",
                "keyId": "e0db55f6-570f-459b-8ce5-181fc812e3e5",
                "secretText": None,
                "startDateTime": "2021-06-03T13:56:43.38Z",
            }
        ],
    },
    {
        "id": "b94b5465-33bf-4ca4-a7a5-989c32688ab6",
        "displayName": "AWS Product Support Prod",
        "passwordCredentials": [],
    },
    {
        "id": "b99d94e1-03fb-47c9-9272-91154ca02a40",
        "displayName": "DigiCert CertCentral",
        "passwordCredentials": [],
    },
    {
        "id": "ba052364-7e28-4039-b7bc-36a107ae9301",
        "displayName": "ReadCube Papers",
        "passwordCredentials": [],
    },
    {
        "id": "bab8e1a3-f57c-4b78-a86c-19bdb8894070",
        "displayName": "cmr-data-app-2",
        "passwordCredentials": [],
    },
    {
        "id": "bb012f7f-dd17-4954-bf92-8f342eb939f1",
        "displayName": "CMR Portal Graph Connection",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Secret 20190516",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "3zb",
                "keyId": "690dd9a6-076b-401f-aa79-e842b222daa4",
                "secretText": None,
                "startDateTime": "2019-05-16T12:58:27.336Z",
            }
        ],
    },
    {
        "id": "bcb0edbf-c24f-4298-b2f5-e08921f9cd78",
        "displayName": "AWS DataRA_1",
        "passwordCredentials": [],
    },
    {
        "id": "bd4b3191-b292-4dcb-b4e6-a0640a34d645",
        "displayName": "Chocolatey",
        "passwordCredentials": [],
    },
    {
        "id": "c3903a02-18eb-4051-81d0-ff2ba6531cef",
        "displayName": "AWS MES-Preprod",
        "passwordCredentials": [],
    },
    {
        "id": "c7ca09f5-5960-479d-8c0b-2c17cde98a0e",
        "displayName": "SAML SSO for Jira by resolution GmbH",
        "passwordCredentials": [],
    },
    {
        "id": "c868643e-7362-4e1c-af90-fdddbd45e962",
        "displayName": "Manufacturing Dev",
        "passwordCredentials": [],
    },
    {
        "id": "ca5277dd-4e25-4ded-a4c1-ed99bff97579",
        "displayName": "part_11_auth",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "part_11_secret",
                "endDateTime": "2024-03-21T09:15:06.553Z",
                "hint": "mmJ",
                "keyId": "90f51d51-cb82-49ac-a2f1-33809bc76cb6",
                "secretText": None,
                "startDateTime": "2022-03-21T09:15:06.553Z",
            }
        ],
    },
    {
        "id": "ca8328f5-d0bc-4773-8f8a-5ba49b39428c",
        "displayName": "AWS Master Billing",
        "passwordCredentials": [],
    },
    {
        "id": "cb6bf70f-02b2-4099-8080-07bde907e000",
        "displayName": "Clinical Data Science Prod",
        "passwordCredentials": [],
    },
    {
        "id": "cb6c7613-9f5f-4896-bed5-97021e67029a",
        "displayName": "test",
        "passwordCredentials": [],
    },
    {
        "id": "cbe160f2-d528-4e47-9a56-97153d5665cf",
        "displayName": "Expensify",
        "passwordCredentials": [],
    },
    {
        "id": "cbe669a5-05aa-4691-ad1f-da6de7d95b02",
        "displayName": "People test",
        "passwordCredentials": [],
    },
    {
        "id": "cc1669e8-aa46-473c-a261-6ec8319751da",
        "displayName": "Kantega SSO for JIRA",
        "passwordCredentials": [],
    },
    {
        "id": "cd3906ec-9248-4c43-bc9f-3b76dd1d8336",
        "displayName": "Microsoft CRM Portals",
        "passwordCredentials": [],
    },
    {
        "id": "d0686652-f7f4-4a52-a6a5-e02241338ed8",
        "displayName": "Test",
        "passwordCredentials": [],
    },
    {
        "id": "d0c86141-a382-44bc-905f-5d73fec2fe11",
        "displayName": "AWS Manuf-Infrastructure",
        "passwordCredentials": [],
    },
    {
        "id": "d0d61170-7b06-42e3-b9e3-d8e2c8023730",
        "displayName": "Mimecast End User Applications",
        "passwordCredentials": [],
    },
    {
        "id": "d1176453-e93e-4fe5-94ad-c2c3ae02d723",
        "displayName": "Mimecast Directory Synchronisation",
        "passwordCredentials": [
            {
                "customKeyIdentifier": "TQBpAG0AZQBjAGEAcwB0AEQAaQByAFMAeQBuAGMA",
                "displayName": None,
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": None,
                "keyId": "8eec5bf4-1706-4ec9-ad8f-1bf25462bc36",
                "secretText": None,
                "startDateTime": "2019-03-29T10:41:02.8291334Z",
            }
        ],
    },
    {
        "id": "d2894e86-bdcd-461a-961c-4eab813c77cc",
        "displayName": "Office_365_Test",
        "passwordCredentials": [
            {
                "customKeyIdentifier": "VABlAHMAdAA=",
                "displayName": None,
                "endDateTime": "2018-04-05T12:34:30.014Z",
                "hint": None,
                "keyId": "304226f0-43e8-4306-bc38-a2794f570e69",
                "secretText": None,
                "startDateTime": "2017-04-05T12:35:53.5984417Z",
            }
        ],
    },
    {
        "id": "d328b33f-b340-4f1c-ae78-a18140106699",
        "displayName": "Auth Dev",
        "passwordCredentials": [],
    },
    {
        "id": "d6152efd-758e-478e-9cbb-93b50dfe5187",
        "displayName": "BIPI Prod",
        "passwordCredentials": [],
    },
    {
        "id": "d793326f-8cd5-48c4-8207-9500200b47d1",
        "displayName": "Processed Videos Dev",
        "passwordCredentials": [],
    },
    {
        "id": "d8f9d84f-52d8-4f44-b139-07a8c2b57857",
        "displayName": "VC MyVersius",
        "passwordCredentials": [],
    },
    {
        "id": "da88c3a6-0de7-40b0-9346-bd7d69262fd5",
        "displayName": "PRTG Monitoring",
        "passwordCredentials": [
            {
                "customKeyIdentifier": "UABSAFQARwA=",
                "displayName": None,
                "endDateTime": "2021-06-17T13:01:02.814Z",
                "hint": None,
                "keyId": "a387f7e1-bd67-4254-988a-2979a17b58f6",
                "secretText": None,
                "startDateTime": "2019-06-17T13:01:17.823459Z",
            },
            {
                "customKeyIdentifier": "UABSAFQARwAyAA==",
                "displayName": None,
                "endDateTime": "2020-06-17T13:08:57.074Z",
                "hint": None,
                "keyId": "3588ed63-5d4e-488d-ab23-bfd75ea4b64b",
                "secretText": None,
                "startDateTime": "2019-06-17T13:09:05.9443973Z",
            },
        ],
    },
    {
        "id": "dc4fbcbf-f067-483f-b7fb-419798cb1d41",
        "displayName": "DSG SDS Video Databricks",
        "passwordCredentials": [],
    },
    {
        "id": "deadd89a-70ab-48a9-a9b5-1265b810fe79",
        "displayName": "CMR IU authentication",
        "passwordCredentials": [],
    },
    {
        "id": "e0f8fed0-35e7-4702-8540-823e2e568181",
        "displayName": "Auth0 OpenID Connect",
        "passwordCredentials": [],
    },
    {
        "id": "e1545552-a766-422e-8358-26e01f5c8676",
        "displayName": "AWS Main",
        "passwordCredentials": [],
    },
    {
        "id": "e16e1af1-fff5-4e9e-845c-60168290a172",
        "displayName": "Clinical Data Science Dev",
        "passwordCredentials": [],
    },
    {
        "id": "e1d961b9-3f9b-4e3f-aaf4-ea2547a8a41b",
        "displayName": "Amazon Web Services (AWS) Test",
        "passwordCredentials": [],
    },
    {
        "id": "e30b7771-e2aa-4fb4-867e-c6c31ab2bdbb",
        "displayName": "VC Dev",
        "passwordCredentials": [],
    },
    {
        "id": "e4ae863a-c256-4aa0-9999-cbf8f970b474",
        "displayName": "Finance automation",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": None,
                "endDateTime": "2099-12-31T12:00:00Z",
                "hint": "eEK",
                "keyId": "d36c8d8e-0ba5-4ddd-9cc6-e1c85dd39041",
                "secretText": None,
                "startDateTime": "2019-02-06T22:36:47.6774052Z",
            }
        ],
    },
    {
        "id": "e75edeb8-40d6-43d4-a306-069985d967aa",
        "displayName": "OutOfOfficeStatus",
        "passwordCredentials": [
            {
                "customKeyIdentifier": "cABhAHMAcwB3AG8AcgBkAA==",
                "displayName": None,
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": None,
                "keyId": "44e00361-5ce4-4ad4-9672-dd718be76005",
                "secretText": None,
                "startDateTime": "2018-09-08T19:15:56.3298648Z",
            }
        ],
    },
    {
        "id": "e7646e9e-f9f7-4ef1-8cac-174668f8322c",
        "displayName": "VC Sandbox",
        "passwordCredentials": [],
    },
    {
        "id": "e82cb6df-9a75-4054-a556-346fad0cd705",
        "displayName": "VC Prod",
        "passwordCredentials": [],
    },
    {
        "id": "e87aca0c-9204-4062-ba6b-bb6eacf99f10",
        "displayName": "Docusign (Demo) OLD",
        "passwordCredentials": [],
    },
    {
        "id": "e998b024-1de9-44e3-86d2-4f6121436de1",
        "displayName": "jupyterhub_telemetry",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": None,
                "endDateTime": "2099-12-31T12:00:00Z",
                "hint": "lvo",
                "keyId": "6218e48d-fbab-470d-a20d-2db16200e34c",
                "secretText": None,
                "startDateTime": "2018-05-08T09:39:42.2812058Z",
            }
        ],
    },
    {
        "id": "ed2191d9-a372-4ba3-8e5c-2b26b8866adb",
        "displayName": "tf-toc-test",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Password uploaded on Mon Nov 02 2020",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "9ia",
                "keyId": "40eeb963-b428-415e-ab65-f0fcf094b573",
                "secretText": None,
                "startDateTime": "2020-11-02T21:26:34.694Z",
            }
        ],
    },
    {
        "id": "edc0f4e9-3f7b-4e6e-a7d6-bce7483f8608",
        "displayName": "Oracle PBCS",
        "passwordCredentials": [],
    },
    {
        "id": "ee409f54-c35d-4c5e-864c-a1e3aee460cc",
        "displayName": "DevOps Sandbox",
        "passwordCredentials": [],
    },
    {
        "id": "ef51ad53-e8a7-4104-94c8-08fd67b685a2",
        "displayName": "DSG BI Databricks",
        "passwordCredentials": [],
    },
    {
        "id": "f1ce49aa-d022-4657-b055-ce88860724b5",
        "displayName": "AWS MES-Prod",
        "passwordCredentials": [],
    },
    {
        "id": "f325fb97-9a1c-4371-b0d2-34e92e00371c",
        "displayName": "PRTG",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "PRTG",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "Hi7",
                "keyId": "5044a688-15e9-4ba1-b005-f3427000ff91",
                "secretText": None,
                "startDateTime": "2020-10-31T23:00:32.757Z",
            }
        ],
    },
    {
        "id": "f3c6d768-839e-4825-8430-5ff35ef9f553",
        "displayName": "My Android App",
        "passwordCredentials": [],
    },
    {
        "id": "f3f5a825-c97b-4db9-a296-44dad2f20f73",
        "displayName": "SproutSocial",
        "passwordCredentials": [],
    },
    {
        "id": "f6fa5c0b-9475-4ed7-97f8-5683cba9336a",
        "displayName": "SocialTalent",
        "passwordCredentials": [],
    },
    {
        "id": "f7c30f5a-85c6-4873-a811-1ffa10bf2a4a",
        "displayName": "Auth0 AAD Integration DEV",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Auth0 test",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "LYD",
                "keyId": "b82c0916-fdb1-4ecf-988b-66702e257069",
                "secretText": None,
                "startDateTime": "2020-07-29T15:23:38.459Z",
            }
        ],
    },
    {
        "id": "f9ea208b-da66-4df5-b45f-2ce529a84296",
        "displayName": "Merchandise Portal",
        "passwordCredentials": [],
    },
    {
        "id": "fb497875-6d21-4156-a0b5-b22c6c0a55b9",
        "displayName": "AWS Cognito",
        "passwordCredentials": [],
    },
    {
        "id": "fc305801-890e-4660-8db8-249c0778c808",
        "displayName": "Greenhouse Onboarding",
        "passwordCredentials": [],
    },
    {
        "id": "fc3888bd-a158-41d6-9005-3c7e60843152",
        "displayName": "Codebeamer",
        "passwordCredentials": [],
    },
    {
        "id": "fcfc5319-79dd-4874-986b-10700c55b1cf",
        "displayName": "ADOIT",
        "passwordCredentials": [],
    },
    {
        "id": "fdd591bf-d6e7-4ee3-913d-04a596183d3b",
        "displayName": "IT Sandbox",
        "passwordCredentials": [],
    },
    {
        "id": "fe59d972-0dab-4ebf-a36b-1b02bbe43d4a",
        "displayName": "GroupMembershipMSGraph",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "groups",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "10_",
                "keyId": "be9322cb-294f-4af3-9af7-d47f317b0a8f",
                "secretText": None,
                "startDateTime": "2021-04-05T16:49:34.899Z",
            },
            {
                "customKeyIdentifier": None,
                "displayName": "Group Membership ",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "-X4",
                "keyId": "f5e052e0-2685-42c7-922d-9bdf1ec46810",
                "secretText": None,
                "startDateTime": "2020-07-06T14:24:29.141Z",
            },
        ],
    },
    {
        "id": "fef29bd0-c813-48bb-a8d0-93e10d5b693f",
        "displayName": "Auth0 production",
        "passwordCredentials": [
            {
                "customKeyIdentifier": None,
                "displayName": "Auth 0 prod client secret",
                "endDateTime": "2299-12-31T00:00:00Z",
                "hint": "p6p",
                "keyId": "9a874f25-2972-4862-87b4-fe36271e4db8",
                "secretText": None,
                "startDateTime": "2020-09-29T16:52:25.949Z",
            }
        ],
    },
]






for app in graph_apps_data:
    # print(app["displayName"])
    if app["passwordCredentials"]:
        print(app["displayName"])
        for secret in app["passwordCredentials"]:
            app_secret_expiry = datetime.date.today()
            secret_display_name = (
                secret["displayName"] if secret["displayName"] else "Not specified"
            )
            secret_end_date = secret["endDateTime"].split("T", 1)[0]
            app_secret_expiry = datetime.datetime.strptime(
                secret_end_date, "%Y-%m-%d"
            ).date()

            print(
                secret_display_name
                + " "
                + secret["keyId"]
                + " "
                + str(app_secret_expiry)
            )
