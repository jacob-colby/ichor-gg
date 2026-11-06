---
type: smite-build
god: Mordred
mode: Conquest
builds:
- source: community
  aspect: Aspect of Rage
  aspect_pick_rate: 0.04
  aspect_win_rate: 0.75
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.24
    win_rate: 0.63
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.23
      win_rate: 0.5
    - name: Bragi's Harp
      pick_rate: 0.16
      win_rate: 0.61
  - name: Sanguine Lash
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.8
    - name: Berserker's Shield
      pick_rate: 0.09
      win_rate: 0.7
  - name: Bracer of The Abyss
    pick_rate: 0.11
    win_rate: 0.75
    alternates:
    - name: Brawler’s Beat Stick
      pick_rate: 0.11
      win_rate: 0.58
    - name: Nimble Ring
      pick_rate: 0.09
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.16
    win_rate: 0.47
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.11
      win_rate: 0.75
    - name: Magi's Cloak
      pick_rate: 0.11
      win_rate: 0.75
  - name: Contagion
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Xibalban Effigy
      pick_rate: 0.07
      win_rate: 0.71
    - name: Kinetic Cuirass
      pick_rate: 0.05
      win_rate: 1.0
  - name: Shell of Rebuke
    pick_rate: 0.07
    win_rate: 0.75
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.5
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.75
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.32
    win_rate: 0.66
  - name: Hunter's Cowl
    pick_rate: 0.27
    win_rate: 0.63
  - name: Bluestone Pendant
    pick_rate: 0.23
    win_rate: 0.52
  source_url: https://smitebrain.com/gods/mordred/
  last_verified: '2026-11-06'
  god_win_rate: 0.5855855855855856
  god_matches_won: 65
  god_matches_played: 111
  god_division: obsidian
  god_window_start: '2026-11-03'
  god_window_end: '2026-11-06'
  god_matches_analyzed: 2859
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Magi's Cloak
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Magi's Cloak
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s
    Revenge, Shield Splitter, Gluttonous Grimoire, Soul Gem, Breastplate of Valor,
    The Reaper, Shield of the Phoenix, Draconic Scale, Runeforged Hammer, Oni Hunter''s
    Garb, Spear of Desolation, Erosion, Eye of Providence, Hydra''s Lament, The Crusher,
    Midgardian Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s Hide, Heartseeker,
    Helm of Radiance, Mantle Of Discord, Helm of Darkness, Blood-Bound Book, Death
    Metal, Titan''s Bane, Obsidian Shard, Ancile, Avenging Blade, Wyrmskin Hide, Tyrfing,
    Arondight.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.71
      win: 0.8
      pick: 0.12
      fit: 0.26
    Berserker's Shield:
      total: 0.6
      efficiency: 0.66
      win: 0.7
      pick: 0.12
      fit: 0.3
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.4
    Magi's Cloak:
      total: 0.58
      efficiency: 0.53
      win: 0.75
      pick: 0.18
      fit: 0.34
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.54
      win: 0.75
      pick: 0.22
      fit: 0.3
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.47
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Magi's Cloak
  - Hide of the Nemean Lion
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Transcendence
  - Rod of Tahuti
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
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Genji''s
    Guard, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge, Amanita Charm, Soul
    Gem, Gluttonous Grimoire, Spear of Desolation, Shield Splitter, Breastplate of
    Valor, Hydra''s Lament, The Reaper, Ancient Signet, Oni Hunter''s Garb, Blood-Bound
    Book, Death Metal, Helm of Radiance, Runeforged Hammer, Shield of the Phoenix,
    Polynomicon, Obsidian Shard, Heartseeker, Helm of Darkness, Spear of the Magus,
    Draconic Scale, Chronos'' Pendant, The Crusher, Screeching Gargoyle, Erosion,
    Dreamer''s Idol, Doom Orb, Eye of Providence, Jade Scepter, Bancroft''s Talon,
    Midgardian Mail, Soul Reaver, Heartwood Charm, Stone of Binding.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.48
      win: 0.62
      pick: 0.0
      fit: 0.23
    Genji's Guard:
      total: 0.66
      efficiency: 0.71
      win: 0.8
      pick: 0.12
      fit: 0.27
    Berserker's Shield:
      total: 0.58
      efficiency: 0.66
      win: 0.7
      pick: 0.12
      fit: 0.22
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.43
    Transcendence:
      total: 0.49
      efficiency: 0.5
      win: 0.62
      pick: 0.0
      fit: 0.23
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.82
      win: 0.62
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Magi's Cloak
  - Hide of the Nemean Lion
  - Soul Gem
  flex_slots:
  - Hide of the Nemean Lion
  - Magi's Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Genji''s Guard, Rod of Tahuti, Berserker''s Shield, Soul Gem, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Spear of Desolation, Breastplate of Valor,
    Shield Splitter, The Reaper, Shield of the Phoenix, Obsidian Shard, Hydra''s Lament,
    Spear of the Magus, Blood-Bound Book, Oni Hunter''s Garb, Helm of Radiance, Runeforged
    Hammer, The Crusher, Draconic Scale, Screeching Gargoyle, Heartseeker, Dreamer''s
    Idol, Death Metal, Chronos'' Pendant, Helm of Darkness, Ancient Signet, Erosion,
    Eye of Providence, Titan''s Bane, Polynomicon, Midgardian Mail, Doom Orb, Stone
    of Binding, Leviathan''s Hide, Arondight, Jade Scepter.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.71
      win: 0.8
      pick: 0.12
      fit: 0.26
    Berserker's Shield:
      total: 0.59
      efficiency: 0.66
      win: 0.7
      pick: 0.12
      fit: 0.23
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.45
    Magi's Cloak:
      total: 0.57
      efficiency: 0.53
      win: 0.75
      pick: 0.18
      fit: 0.26
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.54
      win: 0.75
      pick: 0.22
      fit: 0.23
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.62
      pick: 0.0
      fit: 0.61
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Magi's Cloak
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Magi's Cloak
  - Hide of the Nemean Lion
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Hide of the Nemean Lion
  - Magi's Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
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
    this god: Genji''s Guard, Amanita Charm, Berserker''s Shield, Soul Gem, Rod of
    Tahuti, The Reaper, Shield of the Phoenix, Jotunn''s Revenge, Gluttonous Grimoire,
    Blood-Bound Book, Shield Splitter, Phoenix Feather, Yogi''s Necklace, Runeforged
    Hammer, Ethereal Staff, Breastplate of Valor, Chandra''s Grace, Oni Hunter''s
    Garb, Draconic Scale, Spear of Desolation, Hydra''s Lament, Bancroft''s Talon,
    Erosion, Bloodforge, Eye of Providence, Regrowth Striders, The Crusher, Midgardian
    Mail, Leviathan''s Hide, Heartseeker, Glorious Pridwen, Screeching Gargoyle, Avenging
    Blade, Death Metal, Titan''s Bane, Helm of Radiance, Sphere of Negation.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.71
      win: 0.8
      pick: 0.12
      fit: 0.23
    Berserker's Shield:
      total: 0.6
      efficiency: 0.66
      win: 0.7
      pick: 0.12
      fit: 0.31
    Magi's Cloak:
      total: 0.57
      efficiency: 0.53
      win: 0.75
      pick: 0.18
      fit: 0.28
    Hide of the Nemean Lion:
      total: 0.58
      efficiency: 0.54
      win: 0.75
      pick: 0.22
      fit: 0.31
    Amanita Charm:
      total: 0.63
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.75
    Soul Gem:
      total: 0.6
      efficiency: 0.58
      win: 0.62
      pick: 0.0
      fit: 0.77
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Magi's Cloak
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Magi's Cloak
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Hide of the Nemean Lion
  - Magi's Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Genji''s Guard, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Soul Gem, Screeching Gargoyle, Stone of Binding,
    The Reaper, Spear of Desolation, Shield Splitter, Avenging Blade, Void Stone,
    Void Shield, The Crusher, Breastplate of Valor, Heartseeker, Obsidian Shard, Shield
    of the Phoenix, Titan''s Bane, Runeforged Hammer, Draconic Scale, Oni Hunter''s
    Garb, Spear of the Magus, Hydra''s Lament, Erosion, Eye of Providence, Dreamer''s
    Idol, Midgardian Mail, Blood-Bound Book, Helm of Radiance, Leviathan''s Hide,
    Mantle Of Discord, Doom Orb, Death Metal.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.71
      win: 0.8
      pick: 0.12
      fit: 0.21
    Berserker's Shield:
      total: 0.59
      efficiency: 0.66
      win: 0.7
      pick: 0.12
      fit: 0.25
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.5
    Magi's Cloak:
      total: 0.57
      efficiency: 0.53
      win: 0.75
      pick: 0.18
      fit: 0.28
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.54
      win: 0.75
      pick: 0.22
      fit: 0.25
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Magi's Cloak
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Tyrfing
  - Bracer of The Abyss
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Bracer of The Abyss
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Genji''s Guard, Berserker''s Shield, Rod of Tahuti, Amanita Charm, Jotunn''s
    Revenge, Tyrfing, Gluttonous Grimoire, Soul Gem, Shield Splitter, Golden Blade,
    Breastplate of Valor, Shield of the Phoenix, Spear of Desolation, Oni Hunter''s
    Garb, The Reaper, Draconic Scale, Toxic Blade, Runeforged Hammer, Hydra''s Lament,
    Shogun''s Ofuda, Erosion, Silverbranch Bow, Pharaoh''s Curse, Eye of Providence,
    Tekko-Kagi, Screeching Gargoyle, Blood-Bound Book, Midgardian Mail, Helm of Radiance,
    Riptalon, Stone of Binding, Lernaean Bow, Leviathan''s Hide, Dominance, The Crusher,
    Obsidian Shard, Nimble Ring.'
  slot_scores:
    Genji's Guard:
      total: 0.64
      efficiency: 0.71
      win: 0.8
      pick: 0.12
      fit: 0.19
    Berserker's Shield:
      total: 0.63
      efficiency: 0.72
      win: 0.7
      pick: 0.12
      fit: 0.4
    Tyrfing:
      total: 0.54
      efficiency: 0.53
      win: 0.62
      pick: 0.0
      fit: 0.5
    Bracer of The Abyss:
      total: 0.56
      efficiency: 0.52
      win: 0.75
      pick: 0.17
      fit: 0.21
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.54
      win: 0.75
      pick: 0.22
      fit: 0.22
    Amanita Charm:
      total: 0.57
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.34
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Bracer of The Abyss
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Magi's Cloak
  - Hide of the Nemean Lion
  - Soul Gem
  flex_slots:
  - Hide of the Nemean Lion
  - Magi's Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Berserker''s
    Shield, Soul Gem, Jotunn''s Revenge, Amanita Charm, Breastplate of Valor, Spear
    of Desolation, Shield of the Phoenix, Gluttonous Grimoire, Screeching Gargoyle,
    Hydra''s Lament, Shield Splitter, Chronos'' Pendant, Oni Hunter''s Garb, Draconic
    Scale, Gladiator''s Shield, Prophetic Cloak, The Reaper, Arondight, Erosion, Blood-Bound
    Book, Helm of Radiance, Eye of Providence, Runeforged Hammer, Midgardian Mail,
    Gem of Focus, Obsidian Shard, Heartwood Charm, Helm of Darkness, Stone of Binding,
    Ancient Signet, Chandra''s Grace, Leviathan''s Hide, Mantle Of Discord, Regrowth
    Striders.'
  slot_scores:
    Genji's Guard:
      total: 0.68
      efficiency: 0.71
      win: 0.8
      pick: 0.12
      fit: 0.41
    Berserker's Shield:
      total: 0.59
      efficiency: 0.66
      win: 0.7
      pick: 0.12
      fit: 0.25
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.46
    Magi's Cloak:
      total: 0.57
      efficiency: 0.53
      win: 0.75
      pick: 0.18
      fit: 0.27
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.54
      win: 0.75
      pick: 0.22
      fit: 0.25
    Soul Gem:
      total: 0.58
      efficiency: 0.58
      win: 0.62
      pick: 0.0
      fit: 0.64
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Magi's Cloak
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Magi's Cloak
  - Hide of the Nemean Lion
  - Soul Gem
  flex_slots:
  - Magi's Cloak
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Berserker''s
    Shield, Soul Gem, Amanita Charm, Gluttonous Grimoire, Jotunn''s Revenge, Spear
    of Desolation, Shield Splitter, Breastplate of Valor, Blood-Bound Book, Helm of
    Radiance, Obsidian Shard, Shield of the Phoenix, The Reaper, Death Metal, Helm
    of Darkness, Ancient Signet, Spear of the Magus, Hydra''s Lament, Runeforged Hammer,
    Oni Hunter''s Garb, Chronos'' Pendant, Draconic Scale, Polynomicon, Dreamer''s
    Idol, Screeching Gargoyle, Erosion, The Crusher, Jade Scepter, Eye of Providence,
    Midgardian Mail, Heartseeker, Doom Orb, Stone of Binding, Ethereal Staff, Leviathan''s
    Hide, Triton''s Conch.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.71
      win: 0.8
      pick: 0.12
      fit: 0.23
    Berserker's Shield:
      total: 0.59
      efficiency: 0.66
      win: 0.7
      pick: 0.12
      fit: 0.23
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.37
    Magi's Cloak:
      total: 0.57
      efficiency: 0.53
      win: 0.75
      pick: 0.18
      fit: 0.26
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.54
      win: 0.75
      pick: 0.22
      fit: 0.23
    Soul Gem:
      total: 0.57
      efficiency: 0.58
      win: 0.62
      pick: 0.0
      fit: 0.6
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Magi's Cloak
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Magi's Cloak
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Magi's Cloak
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Rod of Tahuti, Berserker''s
    Shield, Amanita Charm, Gluttonous Grimoire, Soul Gem, Jotunn''s Revenge, Shield
    Splitter, Spear of Desolation, The Reaper, Breastplate of Valor, Blood-Bound Book,
    Helm of Radiance, Runeforged Hammer, Shield of the Phoenix, Obsidian Shard, Death
    Metal, Oni Hunter''s Garb, Draconic Scale, Helm of Darkness, Hydra''s Lament,
    Spear of the Magus, Ancient Signet, The Crusher, Erosion, Eye of Providence, Polynomicon,
    Heartseeker, Dreamer''s Idol, Chronos'' Pendant, Screeching Gargoyle, Midgardian
    Mail, Stone of Binding, Jade Scepter, Titan''s Bane, Leviathan''s Hide, Mantle
    Of Discord.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.71
      win: 0.8
      pick: 0.12
      fit: 0.21
    Berserker's Shield:
      total: 0.59
      efficiency: 0.66
      win: 0.7
      pick: 0.12
      fit: 0.25
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.38
    Magi's Cloak:
      total: 0.57
      efficiency: 0.53
      win: 0.75
      pick: 0.18
      fit: 0.28
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.54
      win: 0.75
      pick: 0.22
      fit: 0.25
    Amanita Charm:
      total: 0.58
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Berserker's Shield
  - Magi's Cloak
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Shield Splitter
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Amanita Charm, Jotunn''s Revenge, Genji''s
    Guard, Shield Splitter, Gluttonous Grimoire, Berserker''s Shield, Soul Gem, Breastplate
    of Valor, The Reaper, Shield of the Phoenix, Draconic Scale, Runeforged Hammer,
    Oni Hunter''s Garb, Spear of Desolation, Erosion, Eye of Providence, Hydra''s
    Lament, The Crusher, Midgardian Mail, Stone of Binding, Screeching Gargoyle, Leviathan''s
    Hide, Heartseeker, Helm of Radiance, Mantle Of Discord, Helm of Darkness, Blood-Bound
    Book, Death Metal, Titan''s Bane, Obsidian Shard, Ancile, Avenging Blade, Wyrmskin
    Hide, Tyrfing, Arondight.'
  slot_scores:
    Genji's Guard:
      total: 0.65
      efficiency: 0.71
      win: 0.8
      pick: 0.12
      fit: 0.26
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.65
      win: 0.62
      pick: 0.0
      fit: 0.4
    Shield Splitter:
      total: 0.56
      efficiency: 0.58
      win: 0.62
      pick: 0.0
      fit: 0.51
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.22
      fit: 0.57
    Freya's Tears:
      total: 0.5
      efficiency: 0.61
      win: 0.47
      pick: 0.27
      fit: 0.42
    Amanita Charm:
      total: 0.59
      efficiency: 0.68
      win: 0.62
      pick: 0.0
      fit: 0.47
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
