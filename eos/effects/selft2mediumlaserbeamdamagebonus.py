# selfT2MediumLaserBeamDamageBonus
#
# Used by:
# Skill: Medium Beam Laser Specialization
type = "passive"


def handler(fit, skill, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Beam Laser Specialization"),
                                  "damageMultiplier", skill.getModifiedItemAttr("damageMultiplierBonus") * skill.level)
