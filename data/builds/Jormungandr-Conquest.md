---
type: smite-build
god: Jormungandr
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Unyielding
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.62
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.46
    win_rate: 0.59
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.09
      win_rate: 0.5
    - name: Eye of Erebus
      pick_rate: 0.08
      win_rate: 0.5
  - name: Ethereal Staff
    pick_rate: 0.16
    win_rate: 0.61
    alternates:
    - name: Gladiator's Shield
      pick_rate: 0.12
      win_rate: 0.67
    - name: Prophetic Cloak
      pick_rate: 0.11
      win_rate: 0.58
  - name: Soul Reaver
    pick_rate: 0.1
    win_rate: 0.65
    alternates:
    - name: Ethereal Staff
      pick_rate: 0.16
      win_rate: 0.44
    - name: Gladiator's Shield
      pick_rate: 0.1
      win_rate: 0.69
  - name: Gladiator's Shield
    pick_rate: 0.12
    win_rate: 0.74
    alternates:
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.67
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.29
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.57
    alternates:
    - name: Soul Reaver
      pick_rate: 0.1
      win_rate: 0.47
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.56
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.73
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.1
      win_rate: 0.5
    - name: Glorious Pridwen
      pick_rate: 0.05
      win_rate: 0.8
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.51
    win_rate: 0.64
  - name: Bluestone Pendant
    pick_rate: 0.2
    win_rate: 0.66
  - name: Bumba's Spear
    pick_rate: 0.06
    win_rate: 0.0
  source_url: https://smitebrain.com/gods/jormungandr/
  last_verified: '2026-09-29'
  god_win_rate: 0.5964912280701754
  god_matches_won: 102
  god_matches_played: 171
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-29'
  god_matches_analyzed: 8229
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Gladiator's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Kinetic Cuirass, Shield Splitter, Breastplate of Valor, Golden Blade, Runeforged
    Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of Providence, Lernaean
    Bow, Draconic Scale, Shogun''s Ofuda, Hydra''s Lament, Shield of the Phoenix,
    Stone of Binding, Tyrfing, Nimble Ring, Helm of Radiance, Gluttonous Grimoire,
    Magi''s Cloak, Avenging Blade, Mantle Of Discord, Screeching Gargoyle, Midgardian
    Mail, Bragi''s Harp, Tekko-Kagi, Daybreak Gavel, Spear of Desolation, Heartseeker,
    Rod of Asclepius, Leviathan''s Hide, Void Shield, Stampede, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.26
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.31
    Gladiator's Shield:
      total: 0.56
      efficiency: 0.39
      win: 0.74
      pick: 0.2
      fit: 0.5
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.58
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Genji's Guard
  - Gladiator's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Glorious Pridwen
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Gladiator's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge,
    Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius, Golden Blade, Soul Gem,
    Runeforged Hammer, Breastplate of Valor, Shield Splitter, Eye of the Storm, Pharaoh''s
    Curse, The Reaper, Yogi''s Necklace, Lernaean Bow, Erosion, Shogun''s Ofuda, Hydra''s
    Lament, Gluttonous Grimoire, Eye of Providence, Phoenix Feather, Tyrfing, Chandra''s
    Grace, Riptalon, Draconic Scale, Nimble Ring, Avenging Blade, Lifebinder, Helm
    of Radiance, Stone of Binding, Daybreak Gavel, Midgardian Mail, Bragi''s Harp,
    Tekko-Kagi, Sphere of Negation.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.23
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.32
    Gladiator's Shield:
      total: 0.56
      efficiency: 0.39
      win: 0.74
      pick: 0.2
      fit: 0.51
    Glorious Pridwen:
      total: 0.6
      efficiency: 0.38
      win: 0.8
      pick: 0.15
      fit: 0.67
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.76
  community_ordered:
  - Genji's Guard
  - Gladiator's Shield
  - Glorious Pridwen
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Berserker's Shield
  - Gladiator's Shield
  - Jotunn's Revenge
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Gladiator's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Stone of Binding, Avenging Blade, Screeching Gargoyle, Kinetic Cuirass, Gluttonous
    Grimoire, Void Shield, Breastplate of Valor, Spear of Desolation, Spear of the
    Magus, Void Stone, Heartseeker, Shield Splitter, Soul Gem, Tekko-Kagi, Obsidian
    Shard, Runeforged Hammer, Silverbranch Bow, Golden Blade, Toxic Blade, Titan''s
    Bane, The Crusher, Eye of the Storm, Hydra''s Lament, Lernaean Bow, Erosion, Nimble
    Ring, Pharaoh''s Curse, The Reaper, Helm of Radiance, Eye of Providence, Shield
    of the Phoenix, Draconic Scale, Doom Orb, Shogun''s Ofuda, Tyrfing.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.66
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.2
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.37
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.39
      win: 0.74
      pick: 0.2
      fit: 0.4
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.47
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Gladiator's Shield
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Gladiator's Shield — physical protection
    swap_item: Gladiator's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Breastplate of
    Valor, Tyrfing, Shield Splitter, Runeforged Hammer, Soul Gem, Pharaoh''s Curse,
    Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance,
    Eye of Providence, Stone of Binding, Eye of the Storm, Shield of the Phoenix,
    Hydra''s Lament, Toxic Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle,
    Daybreak Gavel, The Reaper, Spear of Desolation, Spear of the Magus, Bragi''s
    Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging
    Blade.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.2
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.3
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Gladiator's Shield
  - Jotunn's Revenge
  - Glorious Pridwen
  flex_slots:
  - Berserker's Shield
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Breastplate of Valor, Amanita Charm, Kinetic Cuirass, Shield
    of the Phoenix, Spear of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul
    Gem, Chronos'' Pendant, Shield Splitter, Nimble Ring, Runeforged Hammer, Helm
    of Radiance, Gluttonous Grimoire, Erosion, Pharaoh''s Curse, Golden Blade, Eye
    of Providence, Stone of Binding, Draconic Scale, Shogun''s Ofuda, Eye of the Storm,
    Arondight, Gem of Focus, Lernaean Bow, Spear of the Magus, Magi''s Cloak, Rod
    of Asclepius, Daybreak Gavel, Mantle Of Discord, Obsidian Shard, Midgardian Mail,
    Tyrfing, Eye of Erebus.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.41
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.39
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.41
    Gladiator's Shield:
      total: 0.57
      efficiency: 0.39
      win: 0.74
      pick: 0.2
      fit: 0.62
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.39
    Glorious Pridwen:
      total: 0.58
      efficiency: 0.38
      win: 0.8
      pick: 0.15
      fit: 0.55
  community_ordered:
  - Genji's Guard
  - Gladiator's Shield
  - Glorious Pridwen
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Gladiator's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Breastplate
    of Valor, Eye of the Storm, Gluttonous Grimoire, Golden Blade, Hydra''s Lament,
    Heartseeker, Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi, Eye of Providence,
    Spear of the Magus, Avenging Blade, Shield of the Phoenix, Stone of Binding, Draconic
    Scale, Helm of Radiance, Tyrfing, Titan''s Bane, Soul Gem, The Crusher, Obsidian
    Shard, Pharaoh''s Curse, Magi''s Cloak, The Reaper, Nimble Ring, Shogun''s Ofuda,
    Screeching Gargoyle, Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Silverbranch
    Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.23
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.45
    Gladiator's Shield:
      total: 0.55
      efficiency: 0.39
      win: 0.74
      pick: 0.2
      fit: 0.45
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.52
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Gladiator's Shield
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Gladiator's Shield
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Glorious Pridwen — magical protection
    swap_item: Glorious Pridwen
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Breastplate
    of Valor, Shield Splitter, Spear of the Magus, Spear of Desolation, Nimble Ring,
    Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Golden Blade, Eye
    of the Storm, Hydra''s Lament, Lernaean Bow, Rod of Asclepius, Bragi''s Harp,
    Heartseeker, Erosion, Pharaoh''s Curse, Tekko-Kagi, Stone of Binding, Eye of Providence,
    Tyrfing, Shield of the Phoenix, Draconic Scale, Shogun''s Ofuda, Jade Scepter,
    Doom Orb, Silverbranch Bow, Wish-Granting Pearl, Avenging Blade, Death Metal,
    Chronos'' Pendant, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.18
      fit: 0.2
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.35
    Gladiator's Shield:
      total: 0.54
      efficiency: 0.39
      win: 0.74
      pick: 0.2
      fit: 0.4
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  - Gladiator's Shield
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s
    Revenge, Kinetic Cuirass, Shield Splitter, Breastplate of Valor, Golden Blade,
    Runeforged Hammer, Eye of the Storm, Erosion, Pharaoh''s Curse, Eye of Providence,
    Lernaean Bow, Draconic Scale, Shogun''s Ofuda, Hydra''s Lament, Shield of the
    Phoenix, Stone of Binding, Tyrfing, Nimble Ring, Helm of Radiance, Gluttonous
    Grimoire, Magi''s Cloak, Avenging Blade, Mantle Of Discord, Screeching Gargoyle,
    Midgardian Mail, Bragi''s Harp, Tekko-Kagi, Daybreak Gavel, Spear of Desolation,
    Heartseeker, Rod of Asclepius, Leviathan''s Hide, Void Shield, Stampede, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.58
    Shield Splitter:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.42
      efficiency: 0.61
      win: 0.29
      pick: 0.15
      fit: 0.43
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Freya's Tears
  starter: *id001
---
