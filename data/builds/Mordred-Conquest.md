---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.7
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.37
    win_rate: 0.47
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.31
      win_rate: 0.52
    - name: Bracer of The Abyss
      pick_rate: 0.09
      win_rate: 0.56
  - name: Sanguine Lash
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Shield of the Phoenix
      pick_rate: 0.09
      win_rate: 0.44
    - name: Gladiator's Shield
      pick_rate: 0.08
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.09
    win_rate: 0.42
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.12
      win_rate: 0.55
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.48
  - name: Rod of Tahuti
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.17
      win_rate: 0.53
    - name: Kinetic Cuirass
      pick_rate: 0.06
      win_rate: 0.67
  - name: Hide of the Nemean Lion
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.12
      win_rate: 0.64
    - name: Draconic Scale
      pick_rate: 0.06
      win_rate: 0.8
  - name: Medal of Defense
    pick_rate: 0.06
    win_rate: 0.44
    alternates:
    - name: Olmec Blue
      pick_rate: 0.05
      win_rate: 0.63
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.63
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.4
    win_rate: 0.59
  - name: Bluestone Pendant
    pick_rate: 0.23
    win_rate: 0.35
  - name: Leather Cowl
    pick_rate: 0.16
    win_rate: 0.49
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-10-27'
  god_win_rate: 0.5223367697594502
  god_matches_won: 152
  god_matches_played: 291
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-27'
  god_matches_analyzed: 7385
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Kinetic Cuirass, Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Shield Splitter, Breastplate of Valor, Genji''s Guard, Runeforged Hammer,
    Berserker''s Shield, Eye of the Storm, Gluttonous Grimoire, Erosion, Freya''s
    Tears, Eye of Providence, Hydra''s Lament, Stone of Binding, Heartseeker, Spear
    of Desolation, Helm of Radiance, Magi''s Cloak, Spear of the Magus, Soul Gem,
    Avenging Blade, Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Obsidian
    Shard, Titan''s Bane, The Crusher, Daybreak Gavel, Leviathan''s Hide, Shield of
    the Phoenix, Void Shield, Stampede, Ancile, Rod of Asclepius, Oni Hunter''s Garb,
    The Reaper, Prophetic Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.67
      pick: 0.1
      fit: 0.61
    Shield Splitter:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.56
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.31
      fit: 0.51
    Draconic Scale:
      total: 0.62
      efficiency: 0.5
      win: 0.8
      pick: 0.13
      fit: 0.51
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - Draconic Scale
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Draconic
    Scale, Rod of Tahuti, Kinetic Cuirass, Jotunn''s Revenge, Amanita Charm, Breastplate
    of Valor, Genji''s Guard, Gluttonous Grimoire, Spear of Desolation, Shield Splitter,
    Spear of the Magus, Hydra''s Lament, Runeforged Hammer, Helm of Radiance, Soul
    Gem, Obsidian Shard, Heartseeker, Berserker''s Shield, Eye of the Storm, Rod of
    Asclepius, Wish-Granting Pearl, Doom Orb, Freya''s Tears, Ancient Signet, The
    World Stone, Erosion, Death Metal, Chronos'' Pendant, Jade Scepter, Stone of Binding,
    Eye of Providence, Avenging Blade, Screeching Gargoyle, Magi''s Cloak, Titan''s
    Bane, Helm of Darkness, Triton''s Conch, The Crusher, Daybreak Gavel, Oni Hunter''s
    Garb, Shield of the Phoenix.'
  slot_scores:
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.29
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.1
      fit: 0.46
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.8
      pick: 0.13
      fit: 0.36
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.12
      fit: 0.36
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Draconic Scale
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Draconic Scale, Rod of Tahuti, Kinetic Cuirass, Jotunn''s Revenge, Amanita
    Charm, Gluttonous Grimoire, Spear of Desolation, Breastplate of Valor, Genji''s
    Guard, Soul Gem, Spear of the Magus, Obsidian Shard, Shield Splitter, Runeforged
    Hammer, Helm of Radiance, Freya''s Tears, Berserker''s Shield, Hydra''s Lament,
    Heartseeker, Eye of the Storm, Erosion, Doom Orb, Rod of Asclepius, Eye of Providence,
    Screeching Gargoyle, Stone of Binding, Chronos'' Pendant, The World Stone, Titan''s
    Bane, The Crusher, Dreamer''s Idol, Magi''s Cloak, Jade Scepter, The Reaper, Wish-Granting
    Pearl, Avenging Blade, Daybreak Gavel, Mantle Of Discord, Midgardian Mail, Shield
    of the Phoenix, Ancient Signet.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.1
      fit: 0.48
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.52
      pick: 0.31
      fit: 0.38
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.8
      pick: 0.13
      fit: 0.38
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.12
      fit: 0.34
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - Draconic Scale
  - Rod of Tahuti
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Shifter's Shield
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Jotunn''s
    Revenge, Soul Gem, Rod of Asclepius, Shield of the Phoenix, The Reaper, Runeforged
    Hammer, Shield Splitter, Breastplate of Valor, Genji''s Guard, Gluttonous Grimoire,
    Eye of the Storm, Berserker''s Shield, Ethereal Staff, Yogi''s Necklace, Erosion,
    Eye of Providence, Hydra''s Lament, Phoenix Feather, Chandra''s Grace, Freya''s
    Tears, Heartseeker, Avenging Blade, Spear of Desolation, Lifebinder, Spear of
    the Magus, Glorious Pridwen, Stone of Binding, Helm of Radiance, Midgardian Mail,
    Daybreak Gavel, Obsidian Shard, Titan''s Bane, Sphere of Negation, Magi''s Cloak,
    The Crusher, Screeching Gargoyle.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.67
      pick: 0.1
      fit: 0.6
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.31
      fit: 0.5
    Draconic Scale:
      total: 0.62
      efficiency: 0.5
      win: 0.8
      pick: 0.13
      fit: 0.5
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.51
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Shifter's Shield
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Stone of Binding
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Draconic Scale, Kinetic Cuirass, Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Stone of Binding, Gluttonous Grimoire, Avenging Blade, Screeching
    Gargoyle, Void Shield, Spear of Desolation, Breastplate of Valor, Heartseeker,
    Genji''s Guard, Spear of the Magus, Shield Splitter, Void Stone, Soul Gem, Obsidian
    Shard, Runeforged Hammer, Berserker''s Shield, Titan''s Bane, The Crusher, Eye
    of the Storm, Freya''s Tears, Erosion, The Reaper, Hydra''s Lament, Eye of Providence,
    Helm of Radiance, Doom Orb, The World Stone, Magi''s Cloak, Pendulum Blade, Dreamer''s
    Idol, Avatar''s Parashu, Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Rod
    of Asclepius, Shield of the Phoenix.'
  slot_scores:
    Stone of Binding:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.7
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.54
    Shifter's Shield:
      total: 0.51
      efficiency: 0.55
      win: 0.52
      pick: 0.31
      fit: 0.42
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.1
      fit: 0.52
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.8
      pick: 0.13
      fit: 0.42
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Shifter's Shield
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Nimble Ring
  - Draconic Scale
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Kinetic Cuirass, Rod of Tahuti, Berserker''s Shield,
    Jotunn''s Revenge, Amanita Charm, Nimble Ring, Gluttonous Grimoire, Golden Blade,
    Breastplate of Valor, Genji''s Guard, Soul Gem, Riptalon, Tyrfing, Silverbranch
    Bow, Shield Splitter, Runeforged Hammer, Pharaoh''s Curse, Lernaean Bow, Toxic
    Blade, Shogun''s Ofuda, Freya''s Tears, Helm of Radiance, Erosion, Spear of the
    Magus, The Reaper, Spear of Desolation, Stone of Binding, Hydra''s Lament, Eye
    of Providence, Eye of the Storm, Tekko-Kagi, Obsidian Shard, Magi''s Cloak, Heartseeker,
    Daybreak Gavel, Screeching Gargoyle, Midgardian Mail, Mantle Of Discord, Rod of
    Asclepius, Shield of the Phoenix.'
  slot_scores:
    Golden Blade:
      total: 0.48
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.5
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.4
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.26
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.67
      pick: 0.1
      fit: 0.44
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.28
    Draconic Scale:
      total: 0.59
      efficiency: 0.5
      win: 0.8
      pick: 0.13
      fit: 0.34
  community_ordered:
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Kinetic Cuirass, Rod
    of Tahuti, Jotunn''s Revenge, Breastplate of Valor, Genji''s Guard, Amanita Charm,
    Spear of Desolation, Freya''s Tears, Soul Gem, Hydra''s Lament, Screeching Gargoyle,
    Gluttonous Grimoire, Berserker''s Shield, Chronos'' Pendant, Shield Splitter,
    Shield of the Phoenix, Runeforged Hammer, Helm of Radiance, Prophetic Cloak, Gladiator''s
    Shield, Spear of the Magus, Erosion, Eye of Providence, Stone of Binding, Obsidian
    Shard, Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius,
    Eye of Erebus, Mantle Of Discord, Midgardian Mail, Daybreak Gavel, Heartseeker,
    Pendulum Blade, Glorious Pridwen, Chandra''s Grace, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.66
      win: 0.48
      pick: 0.14
      fit: 0.44
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.1
      fit: 0.51
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.8
      pick: 0.13
      fit: 0.41
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.41
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shifter's Shield
  - Spear of Desolation
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Draconic Scale, Rod of Tahuti, Kinetic Cuirass,
    Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Spear of Desolation, Breastplate
    of Valor, Genji''s Guard, Soul Gem, Spear of the Magus, Helm of Radiance, Obsidian
    Shard, Shield Splitter, Runeforged Hammer, Berserker''s Shield, Rod of Asclepius,
    Freya''s Tears, Hydra''s Lament, Eye of the Storm, Chronos'' Pendant, Erosion,
    Jade Scepter, Doom Orb, Heartseeker, Eye of Providence, Wish-Granting Pearl, Stone
    of Binding, The World Stone, Death Metal, Ancient Signet, Helm of Darkness, Screeching
    Gargoyle, Dreamer''s Idol, Magi''s Cloak, Avenging Blade, Ethereal Staff, Triton''s
    Conch, Daybreak Gavel, Mantle Of Discord, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.1
      fit: 0.49
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.52
      pick: 0.31
      fit: 0.39
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.46
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.8
      pick: 0.13
      fit: 0.39
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Draconic Scale, Kinetic Cuirass, Rod
    of Tahuti, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Shield Splitter,
    Breastplate of Valor, Genji''s Guard, Spear of Desolation, Spear of the Magus,
    Runeforged Hammer, Helm of Radiance, Soul Gem, Obsidian Shard, Berserker''s Shield,
    Eye of the Storm, Hydra''s Lament, Rod of Asclepius, Heartseeker, Freya''s Tears,
    Erosion, Eye of Providence, Stone of Binding, Doom Orb, Jade Scepter, Death Metal,
    Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant, The World
    Stone, Helm of Darkness, Titan''s Bane, The Crusher, Ancient Signet, Screeching
    Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail, Shield of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.41
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.67
      pick: 0.1
      fit: 0.52
    Shield Splitter:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.48
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.52
      pick: 0.31
      fit: 0.42
    Draconic Scale:
      total: 0.6
      efficiency: 0.5
      win: 0.8
      pick: 0.13
      fit: 0.42
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Kinetic Cuirass
  - Shifter's Shield
  - Draconic Scale
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Rod of Tahuti
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Kinetic
    Cuirass, Freya''s Tears, Shield Splitter, Genji''s Guard, Breastplate of Valor,
    Runeforged Hammer, Berserker''s Shield, Eye of the Storm, Gluttonous Grimoire,
    Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Hydra''s Lament,
    Stone of Binding, Heartseeker, Spear of Desolation, Helm of Radiance, Magi''s
    Cloak, Spear of the Magus, Soul Gem, Avenging Blade, Mantle Of Discord, Screeching
    Gargoyle, Midgardian Mail, Obsidian Shard, Titan''s Bane, The Crusher, Daybreak
    Gavel, Leviathan''s Hide, Void Shield, Stampede, Ancile, Rod of Asclepius, Oni
    Hunter''s Garb, The Reaper, Prophetic Cloak.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.67
      pick: 0.1
      fit: 0.61
    Shield Splitter:
      total: 0.5
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.42
      pick: 0.14
      fit: 0.47
    Rod of Tahuti:
      total: 0.56
      efficiency: 0.86
      win: 0.5
      pick: 0.12
      fit: 0.19
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.51
  community_ordered:
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  starter: *id001
---
