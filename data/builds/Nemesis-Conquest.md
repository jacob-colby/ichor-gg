---
type: smite-build
god: Nemesis
mode: Conquest
builds:
- source: community
  aspect: Aspect of Justice
  aspect_pick_rate: 0.16
  aspect_win_rate: 0.67
  slot_order:
  - name: Jotunn's Revenge
    pick_rate: 0.49
    win_rate: 0.53
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.25
      win_rate: 0.5
    - name: Avenging Blade
      pick_rate: 0.06
      win_rate: 0.33
  - name: Hydra's Lament
    pick_rate: 0.35
    win_rate: 0.39
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.63
    - name: Jotunn's Revenge
      pick_rate: 0.08
      win_rate: 0.75
  - name: The Reaper
    pick_rate: 0.15
    win_rate: 0.57
    alternates:
    - name: Hydra's Lament
      pick_rate: 0.12
      win_rate: 0.73
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.6
  - name: Heartseeker
    pick_rate: 0.22
    win_rate: 0.7
    alternates:
    - name: The Reaper
      pick_rate: 0.09
      win_rate: 0.63
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.38
  - name: Titan's Bane
    pick_rate: 0.13
    win_rate: 0.8
    alternates:
    - name: Heartseeker
      pick_rate: 0.13
      win_rate: 0.5
    - name: Blinking Abyss
      pick_rate: 0.1
      win_rate: 0.63
  - name: Blinking Abyss
    pick_rate: 0.18
    win_rate: 0.7
    alternates:
    - name: Skeggox
      pick_rate: 0.09
      win_rate: 0.6
    - name: The Reaper
      pick_rate: 0.07
      win_rate: 0.75
  community_starters:
  - name: Bumba's Hammer
    pick_rate: 0.35
    win_rate: 0.64
  - name: Hunter's Cowl
    pick_rate: 0.21
    win_rate: 0.6
  - name: Bumba's Cudgel
    pick_rate: 0.19
    win_rate: 0.5
  source_url: https://smitebrain.com/gods/nemesis/
  last_verified: '2026-08-14'
  god_win_rate: 0.5473684210526316
  god_matches_won: 52
  god_matches_played: 95
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-14'
  god_matches_analyzed: 3454
  starter:
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Gluttonous Grimoire
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: The Crusher, Gluttonous Grimoire, Death Metal, Lernaean Bow, Berserker''s
    Shield, Damaru, Soul Gem, Riptalon, Golden Blade, Tekko-Kagi, Silverbranch Bow,
    Genji''s Guard, Bragi''s Harp, Dominance, Spear of the Magus, Tyrfing, Runeforged
    Hammer, The Cosmic Horror, Bracer of The Abyss, Breastplate of Valor, Pharaoh''s
    Curse, Demon Blade, Obsidian Shard, Spear of Desolation, Deathbringer, Kinetic
    Cuirass, Shogun''s Ofuda, Amanita Charm, Oni Hunter''s Garb, Nimble Ring, Pendulum
    Blade, Shield Splitter, Eye of Providence, Eros'' Bow, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.53
      pick: 0.49
      fit: 0.49
    Death Metal:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.36
    The Crusher:
      total: 0.57
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.54
    Heartseeker:
      total: 0.57
      efficiency: 0.45
      win: 0.7
      pick: 0.37
      fit: 0.54
    Titan's Bane:
      total: 0.6
      efficiency: 0.45
      win: 0.8
      pick: 0.28
      fit: 0.44
  starter: &id001
    base: Bumba's Golden Dagger
    upgrade: Bumba's Spear
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - The Crusher
  - Titan's Bane
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Kinetic Cuirass
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Berserker''s Shield, Soul Gem, Gluttonous Grimoire, Shield
    of the Phoenix, Riptalon, Kinetic Cuirass, The Crusher, Rod of Asclepius, Genji''s
    Guard, Pharaoh''s Curse, Oni Hunter''s Garb, Golden Blade, Chandra''s Grace, Blood-Bound
    Book, Breastplate of Valor, Bancroft''s Talon, Runeforged Hammer, Lernaean Bow,
    Death Metal, Shogun''s Ofuda, Phoenix Feather, Freya''s Tears, Spectral Armor,
    Damaru, Erosion, Eye of the Storm, Shield Splitter, Eye of Providence, Lifebinder,
    Spear of the Magus, Draconic Scale, Leviathan''s Hide, Silverbranch Bow, Yogi''s
    Necklace, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.49
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.37
    Titan's Bane:
      total: 0.57
      efficiency: 0.45
      win: 0.8
      pick: 0.28
      fit: 0.27
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.69
    Soul Gem:
      total: 0.56
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.59
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Silverbranch Bow
  - The Crusher
  - Heartseeker
  - Titan's Bane
  flex_slots:
  - Gluttonous Grimoire
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: The Crusher, Gluttonous Grimoire, Soul Gem, Riptalon, Silverbranch
    Bow, Spear of the Magus, Tekko-Kagi, The Cosmic Horror, Berserker''s Shield, Death
    Metal, Lernaean Bow, Obsidian Shard, Damaru, Spear of Desolation, Genji''s Guard,
    Golden Blade, Screeching Gargoyle, Breastplate of Valor, The World Stone, Doom
    Orb, Runeforged Hammer, Pendulum Blade, Dreamer''s Idol, Dominance, Toxic Blade,
    Bracer of The Abyss, Bragi''s Harp, Tyrfing, Pharaoh''s Curse, Stone of Binding,
    Kinetic Cuirass, Void Shield, Amanita Charm, Oni Hunter''s Garb, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.53
      pick: 0.49
      fit: 0.61
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.53
    Silverbranch Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.57
    The Crusher:
      total: 0.59
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.67
    Heartseeker:
      total: 0.59
      efficiency: 0.45
      win: 0.7
      pick: 0.37
      fit: 0.67
    Titan's Bane:
      total: 0.62
      efficiency: 0.45
      win: 0.8
      pick: 0.28
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Berserker's Shield
  - Gluttonous Grimoire
  - Riptalon
  - Silverbranch Bow
  - The Crusher
  - Titan's Bane
  flex_slots:
  - The Crusher
  - Silverbranch Bow
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Riptalon, Gluttonous Grimoire, Berserker''s Shield, The Crusher, Silverbranch
    Bow, Golden Blade, Soul Gem, Lernaean Bow, Tyrfing, Genji''s Guard, Death Metal,
    Damaru, Bracer of The Abyss, Pharaoh''s Curse, Spear of the Magus, Tekko-Kagi,
    Breastplate of Valor, Dominance, Bragi''s Harp, Toxic Blade, The Cosmic Horror,
    Nimble Ring, Runeforged Hammer, Blood-Bound Book, Kinetic Cuirass, Shogun''s Ofuda,
    Bancroft''s Talon, Amanita Charm, Oni Hunter''s Garb, Obsidian Shard, Eros'' Bow,
    Eye of Providence, Spear of Desolation, Demon Blade, Freya''s Tears, Qin''s Blade.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.26
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.37
    Riptalon:
      total: 0.56
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.65
    Silverbranch Bow:
      total: 0.54
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.57
    The Crusher:
      total: 0.55
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.37
    Titan's Bane:
      total: 0.57
      efficiency: 0.45
      win: 0.8
      pick: 0.28
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - The Crusher
  - Titan's Bane
  - Soul Gem
  flex_slots:
  - Breastplate of Valor
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Genji''s Guard, Breastplate
    of Valor, Gluttonous Grimoire, The Crusher, Spear of Desolation, Berserker''s
    Shield, Chronos'' Pendant, Freya''s Tears, Death Metal, Shield of the Phoenix,
    Spear of the Magus, Lernaean Bow, Gem of Focus, Riptalon, The Cosmic Horror, Damaru,
    Screeching Gargoyle, Bracer of The Abyss, Silverbranch Bow, Chandra''s Grace,
    Arondight, Pendulum Blade, Golden Blade, Obsidian Shard, Pharaoh''s Curse, Bragi''s
    Harp, Kinetic Cuirass, Runeforged Hammer, Amanita Charm, Blood-Bound Book, Oni
    Hunter''s Garb, Tekko-Kagi, Bancroft''s Talon, Helm of Radiance, Dominance, Tyrfing.'
  slot_scores:
    Genji's Guard:
      total: 0.57
      efficiency: 0.71
      win: 0.6
      pick: 0.0
      fit: 0.34
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.34
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.66
      win: 0.53
      pick: 0.49
      fit: 0.59
    The Crusher:
      total: 0.54
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.34
    Titan's Bane:
      total: 0.57
      efficiency: 0.45
      win: 0.8
      pick: 0.28
      fit: 0.24
    Soul Gem:
      total: 0.58
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.69
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Berserker's Shield
  - Jotunn's Revenge
  - Death Metal
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Lernaean Bow
  - Berserker's Shield
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: The Crusher, Gluttonous Grimoire, Death Metal, Lernaean
    Bow, Berserker''s Shield, Damaru, Soul Gem, Riptalon, Golden Blade, Tekko-Kagi,
    Silverbranch Bow, Genji''s Guard, Bragi''s Harp, Dominance, Spear of the Magus,
    Tyrfing, Runeforged Hammer, The Cosmic Horror, Bracer of The Abyss, Breastplate
    of Valor, Pharaoh''s Curse, Demon Blade, Obsidian Shard, Spear of Desolation,
    Deathbringer, Kinetic Cuirass, Shogun''s Ofuda, Amanita Charm, Oni Hunter''s Garb,
    Avenging Blade, Nimble Ring, Pendulum Blade, Shield Splitter, Eye of Providence,
    Eros'' Bow.'
  slot_scores:
    Lernaean Bow:
      total: 0.55
      efficiency: 0.54
      win: 0.6
      pick: 0.0
      fit: 0.59
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.25
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.66
      win: 0.53
      pick: 0.49
      fit: 0.49
    Death Metal:
      total: 0.55
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.51
    Gluttonous Grimoire:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.36
    The Crusher:
      total: 0.57
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.54
  starter: *id001
---
