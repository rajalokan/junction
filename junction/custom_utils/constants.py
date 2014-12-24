# Conference Application Choice Fields
CONFERENCE_STATUS_ACCEPTING_CFP = "Accepting Call for Proposals"
CONFERENCE_STATUS_CLOSED_CFP = "Closed for Proposals"
CONFERENCE_STATUS_ACCEPTING_VOTES = "Accepting Votes"
CONFERENCE_STATUS_SCHEDULE_PUBLISHED = "Schedule Published"

CONFERENCE_STATUS_LIST = ((1, CONFERENCE_STATUS_ACCEPTING_CFP),
                          (2, CONFERENCE_STATUS_CLOSED_CFP),
                          (3, CONFERENCE_STATUS_ACCEPTING_VOTES),
                          (4, CONFERENCE_STATUS_SCHEDULE_PUBLISHED),
                          )

# Proposal Application Choice Fields
PROPOSAL_STATUS_DRAFT = "Draft"
PROPOSAL_STATUS_PUBLIC = "Public"
PROPOSAL_STATUS_CANCELLED = "Cancelled"

PROPOSAL_STATUS_LIST = ((1, PROPOSAL_STATUS_DRAFT),
                        (2, PROPOSAL_STATUS_PUBLIC),
                        (3, PROPOSAL_STATUS_CANCELLED),
                        )

PROPOSAL_REVIEW_STATUS_YET_TO_BE_REVIEWED = "Yet to be reviewed"
PROPOSAL_REVIEW_STATUS_SELECTED = "Selected"
PROPOSAL_REVIEW_STATUS_REJECTED = "Rejected"
PROPOSAL_REVIEW_STATUS_ON_HOLD = " On hold"
PROPOSAL_REVIEW_STATUS_WAIT_LISTED = "Wait-listed"

PROPOSAL_REVIEW_STATUS_LIST = ((1, PROPOSAL_REVIEW_STATUS_YET_TO_BE_REVIEWED),
                               (2, PROPOSAL_REVIEW_STATUS_SELECTED),
                               (3, PROPOSAL_REVIEW_STATUS_REJECTED),
                               (4, PROPOSAL_REVIEW_STATUS_ON_HOLD),
                               (5, PROPOSAL_REVIEW_STATUS_WAIT_LISTED),
                               )

PROPOSAL_TARGET_AUDIENCE_BEGINNER = "Beginner"
PROPOSAL_TARGET_AUDIENCE_INTERMEDIATE = "Intermediate"
PROPOSAL_TARGET_AUDIENCE_ADVANCED = "Advanced"

PROPOSAL_TARGET_AUDIENCES = ((1, PROPOSAL_TARGET_AUDIENCE_BEGINNER),
                             (2, PROPOSAL_TARGET_AUDIENCE_INTERMEDIATE),
                             (3, PROPOSAL_TARGET_AUDIENCE_ADVANCED),
                             )

PROPOSAL_USER_VOTE_ROLE_PUBLIC = "Public"
PROPOSAL_USER_VOTE_ROLE_REVIEWER = "Reviewer"

PROPOSAL_USER_VOTE_ROLES = ((1, PROPOSAL_USER_VOTE_ROLE_PUBLIC),
                            (2, PROPOSAL_USER_VOTE_ROLE_REVIEWER),
                            )

PROPOSAL_COMMENT_VISIBILITY_PUBLIC = "Public"
PROPOSAL_COMMENT_VISIBILITY_PRIVATE = "Private"

PROPOSAL_COMMENT_VISIBILITY_OPTIONS = ((1, PROPOSAL_COMMENT_VISIBILITY_PUBLIC),
                                       (2, PROPOSAL_COMMENT_VISIBILITY_PRIVATE),
                                       )