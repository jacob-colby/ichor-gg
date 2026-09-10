---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.17
  aspect_win_rate: 0.0
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.5
    win_rate: 0.5
    alternates:
    - name: Runeforged Hammer
      pick_rate: 0.08
      win_rate: 0.0
    - name: Transcendence
      pick_rate: 0.08
      win_rate: 0.0
  - name: Genji's Guard
    pick_rate: 0.25
    win_rate: 0.33
    alternates:
    - name: Gladiator's Shield
      pick_rate: 0.17
      win_rate: 0.5
    - name: Freya's Tears
      pick_rate: 0.17
      win_rate: 0.5
  - name: Breastplate of Valor
    pick_rate: 0.25
    win_rate: 0.33
    alternates:
    - name: Genji's Guard
      pick_rate: 0.25
      win_rate: 0.67
    - name: Runeforged Hammer
      pick_rate: 0.17
      win_rate: 0.5
  - name: Gladiator's Shield
    pick_rate: 0.17
    win_rate: 1.0
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.0
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 1.0
  - name: Triton's Conch
    pick_rate: 0.18
    win_rate: 0.5
    alternates:
    - name: Brawler’s Beat Stick
      pick_rate: 0.18
      win_rate: 0.5
    - name: Void Shield
      pick_rate: 0.09
      win_rate: 0.0
  - name: Hide of the Nemean Lion
    pick_rate: 0.25
    win_rate: 0.5
    alternates:
    - name: Sundering Echo
      pick_rate: 0.13
      win_rate: 1.0
    - name: Arondight
      pick_rate: 0.13
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.42
    win_rate: 0.4
  - name: Bluestone Pendant
    pick_rate: 0.33
    win_rate: 0.25
  - name: Pendulum of the Ages
    pick_rate: 0.17
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-09-10'
  god_win_rate: 0.3333333333333333
  god_matches_won: 4
  god_matches_played: 12
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-10'
  god_matches_analyzed: 1308
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Shell of Rebuke
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Kinetic Cuirass, Shield Splitter, Eye of the Storm, Avenging Blade, Gluttonous
    Grimoire, Lernaean Bow, Hydra''s Lament, Erosion, Pharaoh''s Curse, Eye of Providence,
    Heartseeker, Draconic Scale, Shogun''s Ofuda, Golden Blade, Shield of the Phoenix,
    Tekko-Kagi, Bragi''s Harp, Rod of Asclepius, Daybreak Gavel, Nimble Ring, Helm
    of Radiance, Midgardian Mail, Stone of Binding, Dominance, Spear of the Magus,
    Titan''s Bane, Death Metal, Leviathan''s Hide, Jade Scepter, The Crusher.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.37
    Gladiator's Shield:
      total: 0.67
      efficiency: 0.39
      win: 1.0
      pick: 0.28
      fit: 0.47
    Shell of Rebuke:
      total: 0.59
      efficiency: 0.28
      win: 1.0
      pick: 0.13
      fit: 0.25
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.26
      fit: 0.56
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Gladiator's Shield
  - Shell of Rebuke
  - Runeforged Hammer
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Shifter's Shield
  - Gladiator's Shield
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
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
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge,
    Kinetic Cuirass, Shield of the Phoenix, Rod of Asclepius, Shield Splitter, Eye
    of the Storm, Soul Gem, Erosion, Ethereal Staff, The Reaper, Eye of Providence,
    Yogi''s Necklace, Draconic Scale, Phoenix Feather, Gluttonous Grimoire, Avenging
    Blade, Pharaoh''s Curse, Shogun''s Ofuda, Lernaean Bow, Hydra''s Lament, Lifebinder,
    Stone of Binding, Midgardian Mail, Helm of Radiance, Chandra''s Grace, Daybreak
    Gavel, Magi''s Cloak, Leviathan''s Hide, Sphere of Negation, Stampede, Heartseeker,
    Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.31
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.5
      pick: 0.5
      fit: 0.54
    Gladiator's Shield:
      total: 0.68
      efficiency: 0.39
      win: 1.0
      pick: 0.28
      fit: 0.51
    Shell of Rebuke:
      total: 0.61
      efficiency: 0.28
      win: 1.0
      pick: 0.13
      fit: 0.33
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.84
  community_ordered:
  - Shifter's Shield
  - Gladiator's Shield
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Shell of Rebuke
  - Gluttonous Grimoire
  - Rod of Tahuti
  flex_slots:
  - Gluttonous Grimoire
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s
    Shield, Avenging Blade, Amanita Charm, Heartseeker, Spear of the Magus, Stone
    of Binding, Obsidian Shard, Spear of Desolation, Tekko-Kagi, Titan''s Bane, Kinetic
    Cuirass, The Crusher, Soul Gem, Screeching Gargoyle, The Reaper, Void Stone, Shield
    Splitter, Doom Orb, Eye of the Storm, The World Stone, Avatar''s Parashu, Hydra''s
    Lament, Lernaean Bow, Dreamer''s Idol, Pendulum Blade, Nimble Ring, Daybreak Gavel,
    Helm of Radiance, Erosion, Pharaoh''s Curse, Rod of Asclepius, Eye of Providence,
    Shield of the Phoenix.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.56
    Gladiator's Shield:
      total: 0.66
      efficiency: 0.39
      win: 1.0
      pick: 0.28
      fit: 0.36
    Shell of Rebuke:
      total: 0.58
      efficiency: 0.28
      win: 1.0
      pick: 0.13
      fit: 0.17
    Gluttonous Grimoire:
      total: 0.51
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.63
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Gladiator's Shield
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Nimble Ring
  - Shell of Rebuke
  flex_slots:
  - Golden Blade
  - Jotunn's Revenge
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
    this god: Rod of Tahuti, Berserker''s Shield, Nimble Ring, Golden Blade, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Tyrfing, Riptalon, Kinetic Cuirass,
    Lernaean Bow, Silverbranch Bow, Toxic Blade, Pharaoh''s Curse, Soul Gem, Shogun''s
    Ofuda, Shield Splitter, Tekko-Kagi, Bragi''s Harp, Eye of the Storm, Hydra''s
    Lament, The Reaper, Daybreak Gavel, Dominance, Avenging Blade, Helm of Radiance,
    Bracer of The Abyss, Rod of Asclepius, Spear of the Magus, Erosion, Shield of
    the Phoenix, Eye of Providence, Qin''s Blade, Vital Amplifier, Heartseeker, Draconic
    Scale, Obsidian Shard.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.19
    Gladiator's Shield:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.28
      fit: 0.34
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.36
    Shell of Rebuke:
      total: 0.58
      efficiency: 0.28
      win: 1.0
      pick: 0.13
      fit: 0.16
  community_ordered:
  - Gladiator's Shield
  - Shell of Rebuke
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gladiator's Shield
  - Shell of Rebuke
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti,
    Berserker''s Shield, Amanita Charm, Spear of Desolation, Hydra''s Lament, Shield
    of the Phoenix, Soul Gem, Chronos'' Pendant, Kinetic Cuirass, Screeching Gargoyle,
    Gluttonous Grimoire, Gem of Focus, Nimble Ring, Eye of Erebus, Helm of Radiance,
    Rod of Asclepius, Shield Splitter, Spear of the Magus, Prophetic Cloak, Chandra''s
    Grace, Eye of the Storm, Daybreak Gavel, Obsidian Shard, Erosion, Pharaoh''s Curse,
    Jade Scepter, Lernaean Bow, Eye of Providence, Wish-Granting Pearl, Avenging Blade,
    Totem of Death, Draconic Scale, Pendulum Blade, Shogun''s Ofuda.'
  slot_scores:
    Berserker's Shield:
      total: 0.51
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.49
    Gladiator's Shield:
      total: 0.7
      efficiency: 0.39
      win: 1.0
      pick: 0.28
      fit: 0.67
    Shell of Rebuke:
      total: 0.58
      efficiency: 0.28
      win: 1.0
      pick: 0.13
      fit: 0.17
    Freya's Tears:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.23
      fit: 0.52
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Gladiator's Shield
  - Shell of Rebuke
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Kinetic Cuirass, Shield Splitter, Eye of the Storm, Avenging Blade,
    Gluttonous Grimoire, Lernaean Bow, Hydra''s Lament, Erosion, Pharaoh''s Curse,
    Eye of Providence, Heartseeker, Draconic Scale, Shogun''s Ofuda, Golden Blade,
    Shield of the Phoenix, Tekko-Kagi, Bragi''s Harp, Rod of Asclepius, Daybreak Gavel,
    Nimble Ring, Helm of Radiance, Midgardian Mail, Stone of Binding, Dominance, Spear
    of the Magus, Titan''s Bane, Death Metal, Leviathan''s Hide, Jade Scepter, The
    Crusher.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.26
      fit: 0.56
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Runeforged Hammer
  starter: *id001
---
