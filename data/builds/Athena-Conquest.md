---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.28
  aspect_win_rate: 0.54
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.18
    win_rate: 0.52
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.16
      win_rate: 0.59
    - name: Stampede
      pick_rate: 0.16
      win_rate: 0.59
  - name: Genji's Guard
    pick_rate: 0.12
    win_rate: 0.55
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.65
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.63
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.6
    - name: Transcendence
      pick_rate: 0.09
      win_rate: 0.61
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.65
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.57
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.62
  - name: Blinking Abyss
    pick_rate: 0.09
    win_rate: 0.66
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.08
      win_rate: 0.59
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.6
  - name: Engraved Guard
    pick_rate: 0.05
    win_rate: 0.54
    alternates:
    - name: Heartseeker
      pick_rate: 0.05
      win_rate: 0.75
    - name: Veve Charm
      pick_rate: 0.04
      win_rate: 0.52
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.22
    win_rate: 0.66
  - name: Selflessness
    pick_rate: 0.22
    win_rate: 0.5
  - name: Bumba's Cudgel
    pick_rate: 0.18
    win_rate: 0.54
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-09-04'
  god_win_rate: 0.564021164021164
  god_matches_won: 533
  god_matches_played: 945
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-04'
  god_matches_analyzed: 11911
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Rod of Tahuti, Kinetic Cuirass, Breastplate
    of Valor, Jotunn''s Revenge, Erosion, Eye of Providence, Draconic Scale, Berserker''s
    Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak,
    Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian
    Mail, Runeforged Hammer, Screeching Gargoyle, Prophetic Cloak, Leviathan''s Hide,
    Void Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy, Void
    Stone, Spear of Desolation, Spectral Armor, Hussar''s Wings, Rod of Asclepius,
    Gladiator''s Shield, Daybreak Gavel, Soul Gem, Doublet of Binding, Hydra''s Lament.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.14
      fit: 0.37
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.6
      pick: 0.12
      fit: 0.25
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.14
      fit: 0.62
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.59
      pick: 0.16
      fit: 0.68
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Freya''s Tears,
    Kinetic Cuirass, Breastplate of Valor, Jotunn''s Revenge, Rod of Asclepius, Soul
    Gem, Berserker''s Shield, Erosion, Eye of Providence, Draconic Scale, Ethereal
    Staff, Phoenix Feather, Gluttonous Grimoire, Yogi''s Necklace, Shield Splitter,
    Chandra''s Grace, Runeforged Hammer, Glorious Pridwen, Eye of the Storm, Lifebinder,
    Midgardian Mail, Stone of Binding, Helm of Radiance, Leviathan''s Hide, Void Shield,
    Magi''s Cloak, Ancile, Oni Hunter''s Garb, Daybreak Gavel, Sphere of Negation,
    Screeching Gargoyle, Void Stone, Mantle Of Discord, Spectral Armor, Gladiator''s
    Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.14
      fit: 0.34
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.76
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.63
      pick: 0.14
      fit: 0.54
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.59
      pick: 0.16
      fit: 0.66
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Freya''s Tears,
    Breastplate of Valor, Stone of Binding, Gluttonous Grimoire, Kinetic Cuirass,
    Screeching Gargoyle, Spear of Desolation, Void Shield, Spear of the Magus, Soul
    Gem, Void Stone, Obsidian Shard, Avenging Blade, Berserker''s Shield, Erosion,
    Shield Splitter, Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom
    Orb, Helm of Radiance, Runeforged Hammer, The World Stone, Titan''s Bane, Magi''s
    Cloak, The Crusher, Dreamer''s Idol, Eye of the Storm, Mantle Of Discord, Midgardian
    Mail, The Reaper, Daybreak Gavel, Rod of Asclepius, Leviathan''s Hide, Hydra''s
    Lament.'
  slot_scores:
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.74
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.65
      pick: 0.14
      fit: 0.26
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.6
      pick: 0.12
      fit: 0.47
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.14
      fit: 0.43
    Heartseeker:
      total: 0.6
      efficiency: 0.47
      win: 0.75
      pick: 0.15
      fit: 0.58
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Book of Thoth
  - Berserker's Shield
  - Breastplate of Valor
  - Nimble Ring
  - Heartseeker
  flex_slots:
  - Golden Blade
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Breastplate of Valor, Jotunn''s
    Revenge, Freya''s Tears, Amanita Charm, Nimble Ring, Kinetic Cuirass, Golden Blade,
    Gluttonous Grimoire, Tyrfing, Shield Splitter, Soul Gem, Runeforged Hammer, Pharaoh''s
    Curse, Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm
    of Radiance, Eye of Providence, Stone of Binding, Eye of the Storm, Shield of
    the Phoenix, Hydra''s Lament, Toxic Blade, Draconic Scale, Magi''s Cloak, Screeching
    Gargoyle, Daybreak Gavel, The Reaper, Spear of Desolation, Spear of the Magus,
    Bragi''s Harp, Midgardian Mail, Mantle Of Discord, Tekko-Kagi, Rod of Asclepius,
    Avenging Blade.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.54
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.62
      pick: 0.13
      fit: 0.04
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.65
      pick: 0.14
      fit: 0.2
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.3
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.75
      pick: 0.15
      fit: 0.34
  community_ordered:
  - Book of Thoth
  - Breastplate of Valor
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Heartseeker
  - Amanita Charm
  flex_slots:
  - Heartseeker
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Jotunn''s Revenge, Rod of Tahuti, Amanita Charm, Kinetic Cuirass, Shield of the
    Phoenix, Spear of Desolation, Hydra''s Lament, Screeching Gargoyle, Soul Gem,
    Chronos'' Pendant, Shield Splitter, Berserker''s Shield, Prophetic Cloak, Erosion,
    Helm of Radiance, Runeforged Hammer, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Draconic Scale, Stone of Binding, Eye of the Storm, Arondight, Gem of
    Focus, Magi''s Cloak, Rod of Asclepius, Eye of Erebus, Spear of the Magus, Mantle
    Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel, Chandra''s Grace,
    Obsidian Shard, Leviathan''s Hide, Jade Scepter, Void Shield.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.62
      pick: 0.13
      fit: 0.1
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.65
      pick: 0.14
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.12
      fit: 0.46
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.14
      fit: 0.64
    Heartseeker:
      total: 0.56
      efficiency: 0.47
      win: 0.75
      pick: 0.15
      fit: 0.33
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Book of Thoth
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Heartseeker
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Breastplate
    of Valor, Freya''s Tears, Berserker''s Shield, Amanita Charm, Kinetic Cuirass,
    Shield Splitter, Runeforged Hammer, Golden Blade, Eye of the Storm, Gluttonous
    Grimoire, Hydra''s Lament, Tyrfing, Lernaean Bow, Erosion, Spear of Desolation,
    Tekko-Kagi, Spear of the Magus, Eye of Providence, Avenging Blade, Shield of the
    Phoenix, Stone of Binding, Draconic Scale, Helm of Radiance, Soul Gem, Titan''s
    Bane, Silverbranch Bow, The Crusher, Obsidian Shard, Pharaoh''s Curse, Magi''s
    Cloak, Toxic Blade, The Reaper, Nimble Ring, Shogun''s Ofuda, Screeching Gargoyle,
    Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.62
      pick: 0.13
      fit: 0.04
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.65
      pick: 0.14
      fit: 0.23
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.12
      fit: 0.45
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.61
      pick: 0.14
      fit: 0.22
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.14
      fit: 0.38
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.15
      fit: 0.57
  community_ordered:
  - Book of Thoth
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Heartseeker
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Freya''s Tears, Amanita Charm, Kinetic Cuirass, Gluttonous
    Grimoire, Shield Splitter, Spear of Desolation, Spear of the Magus, Runeforged
    Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Berserker''s Shield, Eye of
    the Storm, Hydra''s Lament, Rod of Asclepius, Erosion, Eye of Providence, Shield
    of the Phoenix, Stone of Binding, Draconic Scale, Doom Orb, Jade Scepter, Death
    Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant,
    The World Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet,
    Screeching Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.49
      efficiency: 0.51
      win: 0.62
      pick: 0.13
      fit: 0.18
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.65
      pick: 0.14
      fit: 0.23
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.12
      fit: 0.41
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.61
      pick: 0.14
      fit: 0.18
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.63
      pick: 0.14
      fit: 0.38
    Heartseeker:
      total: 0.59
      efficiency: 0.47
      win: 0.75
      pick: 0.15
      fit: 0.53
  community_ordered:
  - Book of Thoth
  - Breastplate of Valor
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Freya''s
    Tears, Jotunn''s Revenge, Breastplate of Valor, Erosion, Eye of Providence, Draconic
    Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle
    Of Discord, Midgardian Mail, Runeforged Hammer, Screeching Gargoyle, Prophetic
    Cloak, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness,
    Xibalban Effigy, Void Stone, Spear of Desolation, Spectral Armor, Hussar''s Wings,
    Rod of Asclepius, Gladiator''s Shield, Daybreak Gavel, Soul Gem, Doublet of Binding,
    Hydra''s Lament.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.16
      fit: 0.37
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.6
      pick: 0.12
      fit: 0.25
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.63
      pick: 0.14
      fit: 0.62
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.59
      pick: 0.16
      fit: 0.68
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
