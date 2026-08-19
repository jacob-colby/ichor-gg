---
type: smite-build
god: Artio
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Denmother
  aspect_pick_rate: 0.26
  aspect_win_rate: 0.6
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.22
    win_rate: 0.38
    alternates:
    - name: Yogi's Necklace
      pick_rate: 0.11
      win_rate: 0.7
    - name: Gauntlet of Thebes
      pick_rate: 0.1
      win_rate: 0.2
  - name: Genji's Guard
    pick_rate: 0.22
    win_rate: 0.57
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.58
    - name: Breastplate of Valor
      pick_rate: 0.11
      win_rate: 0.26
  - name: Breastplate of Valor
    pick_rate: 0.12
    win_rate: 0.83
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.49
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.45
  - name: Shell of Rebuke
    pick_rate: 0.12
    win_rate: 0.46
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.53
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.56
  - name: Draconic Scale
    pick_rate: 0.06
    win_rate: 0.33
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.58
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.64
  - name: Legionnaire Armor
    pick_rate: 0.08
    win_rate: 0.67
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.29
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 0.5
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.31
    win_rate: 0.36
  - name: Bluestone Brooch
    pick_rate: 0.27
    win_rate: 0.54
  - name: Selflessness
    pick_rate: 0.13
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/artio/
  last_verified: '2026-08-19'
  god_win_rate: 0.47560975609756095
  god_matches_won: 117
  god_matches_played: 246
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Transcendence
  - Freya's Tears
  flex_slots:
  - Yogi's Necklace
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Berserker''s
    Shield, Jotunn''s Revenge, The Crusher, Gluttonous Grimoire, Shield Splitter,
    Shield of the Phoenix, Oni Hunter''s Garb, Runeforged Hammer, Erosion, Eye of
    the Storm, Eye of Providence, Hydra''s Lament, Spectral Armor, Nimble Ring, Soul
    Gem, Pharaoh''s Curse, Leviathan''s Hide, Golden Blade, Midgardian Mail, Avenging
    Blade, Mantle Of Discord, Death Metal, Stone of Binding, Ancile, Damaru, Screeching
    Gargoyle, Magi''s Cloak, Helm of Radiance, Shogun''s Ofuda, Gladiator''s Shield,
    Hide of the Nemean Lion, Void Shield, Doublet of Binding, Wyrmskin Hide, Draconic
    Scale.'
  slot_scores:
    Yogi's Necklace:
      total: 0.55
      efficiency: 0.57
      win: 0.7
      pick: 0.11
      fit: 0.17
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.57
      pick: 0.3
      fit: 0.31
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.64
      win: 0.83
      pick: 0.19
      fit: 0.31
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.66
    Transcendence:
      total: 0.46
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.22
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.64
      pick: 0.13
      fit: 0.5
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Yogi''s Necklace, Amanita Charm, Freya''s Tears, Shield of the Phoenix,
    Kinetic Cuirass, Soul Gem, Berserker''s Shield, Rod of Tahuti, Gluttonous Grimoire,
    Jotunn''s Revenge, The Crusher, Chandra''s Grace, Ethereal Staff, Rod of Asclepius,
    Runeforged Hammer, Oni Hunter''s Garb, The Reaper, Eye of the Storm, Erosion,
    Shield Splitter, Phoenix Feather, Eye of Providence, Hydra''s Lament, Spectral
    Armor, Golden Blade, Pharaoh''s Curse, Leviathan''s Hide, Avenging Blade, Nimble
    Ring, Midgardian Mail, Blood-Bound Book, Lifebinder, Glorious Pridwen, Riptalon,
    Bancroft''s Talon, Death Metal, Ancile, Shogun''s Ofuda, Draconic Scale.'
  slot_scores:
    Yogi's Necklace:
      total: 0.6
      efficiency: 0.57
      win: 0.7
      pick: 0.11
      fit: 0.51
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.57
      pick: 0.3
      fit: 0.28
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.64
      win: 0.83
      pick: 0.19
      fit: 0.28
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.66
    Freya's Tears:
      total: 0.57
      efficiency: 0.59
      win: 0.64
      pick: 0.13
      fit: 0.46
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.86
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Freya''s Tears, The Crusher, Gluttonous Grimoire,
    Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm, Soul Gem, Avenging Blade, Berserker''s
    Shield, Stone of Binding, Screeching Gargoyle, Void Shield, The Cosmic Horror,
    Oni Hunter''s Garb, The Reaper, Spear of the Magus, Void Stone, Runeforged Hammer,
    Shield of the Phoenix, Obsidian Shard, Spear of Desolation, Hydra''s Lament, Heartseeker,
    Nimble Ring, Shield Splitter, Spectral Armor, Erosion, Titan''s Bane, Eye of the
    Storm, Eye of Providence, Riptalon, Pharaoh''s Curse, Leviathan''s Hide, Silverbranch
    Bow, Golden Blade, Midgardian Mail, Pendulum Blade, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.3
      fit: 0.22
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.64
      win: 0.83
      pick: 0.19
      fit: 0.22
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.56
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.64
      pick: 0.13
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.58
    The Crusher:
      total: 0.55
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Nimble Ring
  - Freya's Tears
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Yogi''s Necklace, Berserker''s Shield, Nimble Ring,
    Rod of Tahuti, Kinetic Cuirass, Amanita Charm, Gluttonous Grimoire, Golden Blade,
    The Crusher, Pharaoh''s Curse, Jotunn''s Revenge, Riptalon, Oni Hunter''s Garb,
    Soul Gem, Shield of the Phoenix, Tyrfing, Shogun''s Ofuda, Runeforged Hammer,
    Silverbranch Bow, Lernaean Bow, Hydra''s Lament, Spectral Armor, Erosion, Shield
    Splitter, Eye of Providence, Eye of the Storm, Dominance, Leviathan''s Hide, Toxic
    Blade, Midgardian Mail, Mantle Of Discord, Death Metal, Helm of Radiance, Stone
    of Binding, Screeching Gargoyle, Damaru, Ethereal Staff, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.55
    Genji's Guard:
      total: 0.54
      efficiency: 0.69
      win: 0.57
      pick: 0.3
      fit: 0.19
    Berserker's Shield:
      total: 0.53
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.64
      win: 0.83
      pick: 0.19
      fit: 0.19
    Nimble Ring:
      total: 0.53
      efficiency: 0.68
      win: 0.53
      pick: 0.0
      fit: 0.3
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.64
      pick: 0.13
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Yogi's Necklace
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge,
    Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass, Amanita Charm, Soul Gem,
    Gluttonous Grimoire, Hydra''s Lament, Berserker''s Shield, The Crusher, Screeching
    Gargoyle, Oni Hunter''s Garb, Chronos'' Pendant, Chandra''s Grace, Nimble Ring,
    Spear of Desolation, Gladiator''s Shield, Erosion, Totem of Death, Spectral Armor,
    Prophetic Cloak, Eye of Providence, Runeforged Hammer, Shield Splitter, Gem of
    Focus, Pharaoh''s Curse, Eye of the Storm, Leviathan''s Hide, Helm of Radiance,
    Midgardian Mail, Arondight, Ethereal Staff, Rod of Asclepius, Mantle Of Discord,
    Death Metal, Stone of Binding, The Cosmic Horror, Draconic Scale.'
  slot_scores:
    Yogi's Necklace:
      total: 0.54
      efficiency: 0.57
      win: 0.7
      pick: 0.11
      fit: 0.13
    Genji's Guard:
      total: 0.59
      efficiency: 0.69
      win: 0.57
      pick: 0.3
      fit: 0.48
    Breastplate of Valor:
      total: 0.68
      efficiency: 0.64
      win: 0.83
      pick: 0.19
      fit: 0.48
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.53
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.64
      pick: 0.13
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Yogi's Necklace
  - Book of Thoth
  - Genji's Guard
  - Breastplate of Valor
  - Transcendence
  - Freya's Tears
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Rod of Tahuti, The Crusher,
    Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s Shield, Kinetic Cuirass,
    Amanita Charm, Runeforged Hammer, Nimble Ring, Hydra''s Lament, Soul Gem, Shield
    Splitter, Oni Hunter''s Garb, Golden Blade, Eye of the Storm, Shield of the Phoenix,
    Pharaoh''s Curse, Spectral Armor, Erosion, The Reaper, Lernaean Bow, Eye of Providence,
    Death Metal, Avenging Blade, Damaru, The Cosmic Horror, Heartseeker, Shogun''s
    Ofuda, Leviathan''s Hide, Spear of the Magus, Titan''s Bane, Dominance, Midgardian
    Mail, Tekko-Kagi, Obsidian Shard, Spear of Desolation, Tyrfing, Draconic Scale.'
  slot_scores:
    Yogi's Necklace:
      total: 0.54
      efficiency: 0.57
      win: 0.7
      pick: 0.11
      fit: 0.12
    Book of Thoth:
      total: 0.42
      efficiency: 0.49
      win: 0.53
      pick: 0.0
      fit: 0.04
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.3
      fit: 0.22
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.64
      win: 0.83
      pick: 0.19
      fit: 0.22
    Transcendence:
      total: 0.46
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.23
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.64
      pick: 0.13
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - The Crusher
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Freya''s Tears, Gluttonous
    Grimoire, The Crusher, Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm, Soul
    Gem, Berserker''s Shield, Nimble Ring, The Cosmic Horror, Oni Hunter''s Garb,
    Runeforged Hammer, Death Metal, Spear of the Magus, Hydra''s Lament, Shield of
    the Phoenix, Shield Splitter, Obsidian Shard, Spear of Desolation, Eye of the
    Storm, Helm of Radiance, Spectral Armor, Erosion, Ethereal Staff, Eye of Providence,
    Rod of Asclepius, The Reaper, Golden Blade, Chronos'' Pendant, Pharaoh''s Curse,
    Jade Scepter, Leviathan''s Hide, Avenging Blade, Midgardian Mail, Damaru, Triton''s
    Conch, Heartseeker, Draconic Scale.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.69
      win: 0.57
      pick: 0.3
      fit: 0.22
    Breastplate of Valor:
      total: 0.64
      efficiency: 0.64
      win: 0.83
      pick: 0.19
      fit: 0.22
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.55
      efficiency: 0.59
      win: 0.64
      pick: 0.13
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.56
    The Crusher:
      total: 0.53
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Crusher
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Rod of Tahuti, Berserker''s
    Shield, Jotunn''s Revenge, The Crusher, Freya''s Tears, Gluttonous Grimoire, Shield
    Splitter, Shield of the Phoenix, Oni Hunter''s Garb, Runeforged Hammer, Erosion,
    Eye of the Storm, Eye of Providence, Hydra''s Lament, Draconic Scale, Spectral
    Armor, Nimble Ring, Soul Gem, Pharaoh''s Curse, Leviathan''s Hide, Golden Blade,
    Midgardian Mail, Avenging Blade, Mantle Of Discord, Death Metal, Stone of Binding,
    Ancile, Damaru, Screeching Gargoyle, Magi''s Cloak, Helm of Radiance, Shogun''s
    Ofuda, Gladiator''s Shield, Hide of the Nemean Lion, Void Shield, Doublet of Binding,
    Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.57
      pick: 0.3
      fit: 0.31
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.36
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.66
    The Crusher:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.38
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.56
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Amanita Charm, Rod
    of Tahuti, Berserker''s Shield, Jotunn''s Revenge, The Crusher, Freya''s Tears,
    Gluttonous Grimoire, Shield Splitter, Shield of the Phoenix, Oni Hunter''s Garb,
    Runeforged Hammer, Erosion, Eye of the Storm, Eye of Providence, Hydra''s Lament,
    Draconic Scale, Spectral Armor, Nimble Ring, Soul Gem, Pharaoh''s Curse, Leviathan''s
    Hide, Golden Blade, Midgardian Mail, Avenging Blade, Mantle Of Discord, Death
    Metal, Stone of Binding, Ancile, Damaru, Screeching Gargoyle, Magi''s Cloak, Helm
    of Radiance, Shogun''s Ofuda, Gladiator''s Shield, Hide of the Nemean Lion, Void
    Shield, Doublet of Binding, Wyrmskin Hide.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.69
      win: 0.57
      pick: 0.3
      fit: 0.31
    Berserker's Shield:
      total: 0.52
      efficiency: 0.66
      win: 0.53
      pick: 0.0
      fit: 0.36
    Breastplate of Valor:
      total: 0.65
      efficiency: 0.64
      win: 0.83
      pick: 0.19
      fit: 0.31
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.64
      win: 0.53
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.53
      pick: 0.0
      fit: 0.66
    Amanita Charm:
      total: 0.54
      efficiency: 0.63
      win: 0.53
      pick: 0.0
      fit: 0.56
  swaps:
  - added: Breastplate of Valor
    removed: The Crusher
    reason: community 83% win over 30 matches (vs 48% on this god), taking the model's
      weakest slot from The Crusher
  starter: *id001
---
